import argparse
from ultralytics import YOLO
from PIL import Image
import os

def run_inference(image_path, output_path):
    """
    Run inference on the given image using YOLOv10.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Directory to save the output image.
    """
    # Check if the image exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return

    # Check if the model weights file exists
    model_path = "best.pt"
    if not os.path.exists(model_path):
        print(f"Error: Model file '{model_path}' not found in the current directory.")
        return

    # Load the YOLO model
    print("Loading YOLO model...")
    model = YOLO(model_path)

    # Run inference
    print("Running inference...")
    results = model(image_path)

    # Save the output image
    output_file = os.path.join(output_path, "output.jpg")
    print(f"Saving results to {output_file}...")
    results[0].plot(save=True, show=False)
    os.rename("runs/detect/predict/image0.jpg", output_file)
    print("Inference complete.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run YOLOv10 inference on an image.")
    parser.add_argument("image_path", type=str, help="Path to the input image.")
    parser.add_argument("output_path", type=str, help="Path to the directory to save the output image.")

    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.output_path, exist_ok=True)

    # Run the inference function
    run_inference(args.image_path, args.output_path)
