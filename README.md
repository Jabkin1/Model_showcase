# Weed Detection in Cabbage Fields Using YOLOv8

This repository contains a pretrained YOLOv8 model designed to detect various weed species in cabbage fields. The model leverages RGB and NIR data, enabling it to process both 3-channel (RGB) and 4-channel (RGB+NIR) images. It achieves state-of-the-art performance, with a mean Average Precision at IoU threshold 0.50 (mAP@50) of **94.9%** across 14 classes.

## Model Features
- **High Accuracy**: The model achieves a remarkable mAP@50 of 94.9%.
- **Versatile Input**: Supports both RGB and NIR-enhanced data for increased flexibility.
- **Multi-Class Detection**: Trained to identify 12 core groups weed species common in cabbage fields as well as combined non-targer groups.

## Requirements
To use this model, ensure you have the following installed:

- Python 3.7 or later
- Required Python libraries:
  - ultralytics
  - numpy
  - opencv-python
  - Pillow

You can install the required libraries using:
```bash
pip install ultralytics numpy opencv-python Pillow
```

## Implementation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Jabkin1/Model_showcase.git
cd Model_showcase
```

### 2. Prepare Your Environment
Ensure your working directory contains:
- The script file (`Model_showcase.py` or similar).
- The pretrained model weights file (`best.pt`).

### 3. Input Image Requirements
- **RGB Images**: Standard 3-channel images.
- **NIR Images**: 4-channel images (RGB + Near-Infrared).

The model will automatically adapt based on the input dimensions.

### 4. Running the Model
Use the provided Python script to run inference on an image. The script requires the following inputs:

- Path to the input image.
- Directory to save the output results.

#### Example Command
```bash
python Model_showcase.py <path_to_image> <output_directory>
```

#### Example Usage
```bash
python Model_showcase.py ./test_images/image.jpg ./output_results
```

The output will include:
- An annotated image with bounding boxes and class labels saved in the specified output directory.

### 5. Evaluation Metrics
The model was evaluated on a diverse dataset of cabbage fields, achieving:
- **mAP@50**: 94.9% across 12 classes.

## Model Training Details
- **Dataset**: Images collected from cabbage fields, combining RGB and NIR channels.
- **Classes**: 12 weed species.
- **Framework**: YOLOv8 using the `ultralytics` library.

## Supported Weed and crop Classes with EPPO codes
1. AMARE
2. VERPE
3. STEME
4. CAPBP
5. SOLNI
6. MERAN
7. CHEXX
8. MATIN
9. SONXX
10. THLAR
11. sagrass (Summer Annual grasses)
12. Ograss (Other grasses)
13. Dicot (Other dicotyledonous)
14. Cabbage


## Troubleshooting
- **Model Not Detecting Properly**: Ensure the input image matches the required format (RGB or RGB+NIR).
- **File Not Found Errors**: Check that the `best.pt` file is in the same directory as the script.
- **Dependencies Issues**: Ensure all required libraries are installed correctly.




