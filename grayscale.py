from PIL import Image
import numpy as np
import os

INPUT_DIR = "input"
OUTPUT_DIR = "grayscale"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):

        name, ext = os.path.splitext(file)
        out_name = f"grayscaled_{name}{ext}"
        out_path = os.path.join(OUTPUT_DIR, out_name)

        # SKIP if already processed
        if os.path.exists(out_path):
            print(f"Skipped (already exists): {file}")
            continue

        path = os.path.join(INPUT_DIR, file)
        img = Image.open(path)
        arr = np.array(img)

        gray = 0.21*arr[:,:,0] + 0.72*arr[:,:,1] + 0.07*arr[:,:,2]
        gray_img = Image.fromarray(gray.astype("uint8"))

        gray_img.save(out_path)
        print(f"Processed: {file}")
