import cv2
import numpy as np
from PIL import Image

def process_image(input_path, output_path):
    # Load image in OpenCV
    img_bgr = cv2.imread(input_path)
    if img_bgr is None:
        raise ValueError("Could not load input image.")
        
    try:
        from rembg import remove
        input_image = Image.open(input_path).convert("RGB")
        output_image = remove(input_image)
        img_bgra = np.array(output_image)
        alpha_channel = img_bgra[:, :, 3]
    except ImportError:
        print("rembg not available. Falling back to OpenCV GrabCut.")
        # GrabCut fallback
        mask = np.zeros(img_bgr.shape[:2], np.uint8)
        bgdModel = np.zeros((1,65), np.float64)
        fgdModel = np.zeros((1,65), np.float64)
        
        # Define a rectangle bounding the person (assuming mostly centered)
        h, w = img_bgr.shape[:2]
        rect = (int(w*0.15), int(h*0.1), int(w*0.7), int(h*0.85))
        
        cv2.grabCut(img_bgr, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
        alpha_channel = mask2 * 255
    
    # 6. Convert to grayscale
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    # 8. Apply light noise reduction
    img_gray = cv2.bilateralFilter(img_gray, d=5, sigmaColor=50, sigmaSpace=50)
    
    # 4 & 5. Boost local contrast using OpenCV CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_contrast = clahe.apply(img_gray)
    
    # 7. Composite onto a pure white background
    white_bg = np.ones_like(img_contrast) * 255
    mask_f = alpha_channel / 255.0
    img_final = (img_contrast * mask_f + white_bg * (1 - mask_f)).astype(np.uint8)
    
    # 9. Save the final processed image
    cv2.imwrite(output_path, img_final)
    print(f"Preprocessed photo saved to {output_path}")

if __name__ == "__main__":
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    process_image(os.path.join(base_dir, "assets", "photo.jpg"), os.path.join(base_dir, "assets", "source-prepped.png"))
