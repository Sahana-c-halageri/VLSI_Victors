# AI-Powered Restoration of Noisy SEM Images for Semiconductor Defect Detection

## Structure

```text
sem_ai_project/
├── run.py
├── requirements.txt
├── README.md
└── models/
```

## Pipeline

Degraded SEM → Preprocessing → DnCNN Restoration → Restored SEM → EfficientNet-B0 → Normal/Defective

## Tools

- Python — development
- PyTorch — deep learning
- DnCNN — image restoration
- EfficientNet-B0 — defect classification
- OpenCV — preprocessing
- NumPy — image/numerical operations
- scikit-image — SSIM/image quality
- scikit-learn — accuracy, precision, recall, F1
- Matplotlib — visualization
- VS Code — development

## Install

```powershell
pip install -r requirements.txt
```

## Run

```powershell
python run.py --image path/to/sem_image.png
```

## Models

Place trained weights in `models/`, for example:

```text
models/
├── dncnn_best.pth
└── defect_classifier_best.pth
```

Only report measured performance values from your actual test dataset.
