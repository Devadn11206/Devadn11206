import cv2
import numpy as np

def convert_to_ascii(image_path, width=120, char_aspect_ratio=0.5, ramp="@%#*+=-:. "):
    # Load grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not load image at {image_path}")
    
    # Calculate new dimensions preserving aspect ratio and font aspect ratio
    original_height, original_width = img.shape
    new_width = width
    
    # Text characters are typically taller than they are wide.
    # char_aspect_ratio is usually width/height of a character in the font. (e.g. 0.5)
    # new_height = int(original_height / original_width * new_width * char_aspect_ratio)
    
    new_height = int((original_height / original_width) * new_width * char_aspect_ratio)
    
    # Resize image
    img_resized = cv2.resize(img, (new_width, new_height))
    
    # Normalize and map to ASCII ramp
    # Ramp goes from dark to light.
    # In OpenCV grayscale, 0 is black, 255 is white.
    
    ascii_matrix = []
    ramp_length = len(ramp)
    for row in img_resized:
        ascii_row = []
        for pixel in row:
            # Scale pixel (0-255) to ramp index (0 to ramp_length-1)
            # Black (0) -> index 0 (dense char)
            # White (255) -> index ramp_length-1 (light char)
            idx = int(pixel / 256.0 * ramp_length)
            ascii_row.append(ramp[idx])
        ascii_matrix.append(ascii_row)
        
    return ascii_matrix

if __name__ == "__main__":
    matrix = convert_to_ascii("../assets/source-prepped.png")
    for row in matrix:
        print("".join(row))
