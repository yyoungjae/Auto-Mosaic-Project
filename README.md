<img width="446" height="369" alt="image" src="https://github.com/user-attachments/assets/44ee8aba-c1cf-49ae-a9fd-5ed7a7b836af" />Auto Mosaic Project
1. Project Overview

Auto Mosaic Processor is a Python-based image processing project that automatically detects faces and applies mosaic (Gaussian blur) to protect privacy.
It uses OpenCV’s Haar Cascade classifier for face detection and processes multiple images in batch mode.
The project is modularized into separate components for loading images, applying mosaic effects, and orchestrating the full pipeline.

2. Demo (Before / After)
Before
After
(Insert original image)	(Insert mosaic-applied result)

You can generate your own demo by placing images in the assets/ folder and checking the processed outputs in output_processed/.

3. Packages Used & Versions

Required dependencies (from requirements.txt):

opencv-python==4.9.0
numpy==1.26.0


These packages are used for image handling, face detection, and performing the mosaic blur.

4. How to Run
1) Install dependencies
pip install -r requirements.txt

2) Prepare input images

Place any JPG/PNG/BMP images in the assets/ folder:

assets/
 ├─ img1.jpg
 ├─ img2.png

3) Run the program
python main.py

4) Check processed results

Outputs will be saved in:

output_processed/
 ├─ mosaic_img1.jpg
 ├─ mosaic_img2.png

5. Main Code Components
✔ main.py — Pipeline Controller

Scans images from assets/

Applies the mosaic algorithm

Saves processed files

Creates output directories when needed


aa863d48-3679-418a-8f92-32b2f92…

✔ processors/loader.py — Image I/O Utility

Loads images using OpenCV

Saves processed images with proper compression settings

Retrieves image file lists from a directory


9ef323df-aa5d-4165-9fb4-5fdc1e3…

✔ processors/blur.py — Face Detection & Mosaic

Uses Haar Cascade to locate faces

Applies Gaussian Blur to detected regions

Returns the processed result


6295c5e4-0f74-4d5b-8b21-29d28ae…

6. Contributors

Team Member A (함태은) — Image loading & saving module (loader.py)

Team Member B (양영재)— Face detection & mosaic algorithm (blur.py)

Team Member C (김민서)— Main pipeline assembly(main.py) and project structure
