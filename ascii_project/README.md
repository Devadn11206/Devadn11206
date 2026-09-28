# Animated ASCII Portrait Generator

This project takes a standard photograph, automatically removes the background, balances the contrast, and converts it into a premium animated ASCII SVG suitable for GitHub profiles.

## Setup

The project uses a Python virtual environment to manage dependencies such as OpenCV, Pillow, and Rembg (for background removal).

### Installation

```bash
cd ascii_project
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
```

*(Note: If `rembg` fails to install due to system restrictions, `prep_photo.py` will gracefully fallback to OpenCV GrabCut).*

## Usage

1. **Place your source image:**
   Save your portrait as `assets/photo.jpg`.

2. **Run preprocessing:**
   This script removes the background and normalizes contrast for optimal ASCII generation.
   ```bash
   python scripts/prep_photo.py
   ```
   *(This outputs `assets/source-prepped.png`)*

3. **Generate the ASCII SVG:**
   This script maps the preprocessed image to a dense ASCII ramp and generates both an animated and static SVG.
   ```bash
   python scripts/generate_svg.py
   ```
   *(This outputs `assets/devanandu-ascii.svg` and `assets/devanandu-ascii-static.svg`)*

## Adding to GitHub Profile README

To embed this into your main profile README, simply use this snippet:

```html
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./ascii_project/assets/devanandu-ascii.svg">
    <source media="(prefers-color-scheme: light)" srcset="./ascii_project/assets/devanandu-ascii-static.svg">
    <img alt="Animated ASCII Identity" src="./ascii_project/assets/devanandu-ascii.svg" width="500">
  </picture>
</div>
```

If GitHub strips the animation styles on certain clients, the image will cleanly degrade to the static ASCII matrix.
