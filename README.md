# Batch Image Processing Pipeline

A Python-based batch image processing system that automatically converts color images to grayscale and then applies Gaussian smoothing.  
The pipeline is designed to handle **multiple images at once**, **skip already processed files**, and **generate clean outputs with dynamic filenames**.

---

## 👨‍💻 Author
**Harish Kumar**

---

## 📌 What This Project Does

This project performs two main operations:

1. **Grayscale Conversion (Luminosity Method)**  
   Converts RGB images to grayscale using the formula:  
   `0.21R + 0.72G + 0.07B`

2. **Gaussian Smoothing**  
   Applies a Gaussian filter using manual convolution to reduce noise and smooth the image.

It is built to work in **batch mode**, meaning you can process **many images at once**.

---

## ⚙️ Key Features

- Process unlimited images at once  
- Automatically skips already processed files  
- Keeps original filenames (with prefixes)  
- No overwriting issues  
- Works on any system (no hardcoded paths)  

---

## 📁 Folder Structure
Image-Processing/
│
├── Input/ -- original color images
├── Grayscale/ -- grayscale outputs
├── Smoothing/ -- smoothed outputs
│
├── grayscale.py
├── smoothing.py
└── requirements.txt

---

## 🔁 How the Pipeline Works

1. Put any number of color images inside the **Input/** folder.
2. Run `grayscale.py`  
   - Reads all images from Input  
   - Converts them to grayscale  
   - Saves them in **Grayscale/** as:  
     `grayscaled_<original_name>`

3. Run `smoothing.py`  
   - Reads all images from Grayscale  
   - Applies Gaussian smoothing  
   - Saves them in **Smoothing/** as:  
     `smoothed_<grayscaled_name>`

4. If you run the code again, it will **skip images that are already processed.**

---

## ▶️ How to Use

### Step 1: Install dependencies
    pip install -r requirements.txt
### Step 2: Add images
    Place any .jpg, .png, or .jpeg images into:
       Input/
### Step 3: Convert to Grayscale
    python grayscale.py
### Step 4: Apply Smoothing
    python smoothing.py

---

## 🧠 Skip Logic (Smart Feature)

Before processing any file, the code checks:
“Does this output file already exist?”
If yes → it skips the image
If no → it processes the image

#### This prevents:

Reprocessing the same image
Overwriting previous results
Wasting time

---

## 📈 Future Improvements

Edge detection
Histogram equalization
GUI interface
Video frame processing
