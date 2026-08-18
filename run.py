import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="SEM restoration and defect inspection")
    parser.add_argument("--image", required=True, help="Path to SEM image")
    args = parser.parse_args()

    image = Path(args.image)
    if not image.exists():
        raise FileNotFoundError(f"Image not found: {image}")

    print("=" * 60)
    print("AI-POWERED SEM INSPECTION")
    print("=" * 60)
    print(f"Input image: {image}")
    print("\nPipeline:")
    print("1. Preprocess SEM image")
    print("2. DnCNN restoration")
    print("3. EfficientNet-B0 defect classification")
    print("4. Report normal/defective result")
    print("\nPlace trained weights inside models/.")

if __name__ == "__main__":
    main()
