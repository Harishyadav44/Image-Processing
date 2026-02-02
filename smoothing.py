import cv2
import numpy as np
import os

INPUT_DIR = "grayscale"
OUTPUT_DIR = "smoothing"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gaussian_kernel(size, sigma):
    k = np.linspace(-(size//2), size//2, size)
    k = np.exp(-0.5*(k/sigma)**2)
    k /= k.sum()
    return np.outer(k, k)

kernel = gaussian_kernel(5, 1.0)

for file in os.listdir(INPUT_DIR):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):

        name, ext = os.path.splitext(file)
        out_name = f"smoothed_{name}{ext}"
        out_path = os.path.join(OUTPUT_DIR, out_name)

        # SKIP if already processed
        if os.path.exists(out_path):
            print(f"Skipped (already exists): {file}")
            continue

        img = cv2.imread(os.path.join(INPUT_DIR, file), 0)
        if img is None:
            continue

        pad = kernel.shape[0]//2
        padded = np.pad(img, [(pad,pad),(pad,pad)], mode="constant")
        out = np.zeros_like(img, dtype=float)

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                out[i,j] = np.sum(kernel * padded[i:i+5, j:j+5])

        cv2.imwrite(out_path, out.astype("uint8"))
        print(f"Processed: {file}")
