# SmartDigit – Handwriting Recognition (MNIST)

> **Domain:** Computer Vision / Deep Learning  
> **Level:** Beginner (Student R&D)  
> **Purpose:** Build and evaluate a minimal neural network for handwritten digit classification using the MNIST dataset

---

## 1. Background & Concept
Handwritten digit recognition is a classic entry point to deep learning and computer vision.  
This project uses MNIST to train a simple fully-connected neural network that learns to classify digits (0–9) based on pixel intensity patterns.

The goal is not to build a complex model, but to understand the basic mechanics of neural networks, image preprocessing and model evaluation.

---

## 2. What the Project Does
- Loads and preprocesses MNIST images  
- Builds a basic ANN with a single hidden layer (128 units)  
- Trains the model for 5 epochs  
- Evaluates on test set (~97% accuracy)  
- Visualizes predictions on sample images  

---

## 3. Project Structure
Handwriting-MNIST/
├── .venv/
├── data/
├── notebooks/
│ └── MNIST_ANN.ipynb
├── src/
│ ├── model.py
│ ├── train.py
│ └── utils.py
├── .gitignore
├── requirements.txt
└── README.md

---

## 4. Run Instructions

### Create/activate virtual environment
```bash
.venv\Scripts\activate    # Windows
source .venv/bin/activate # Mac/Linux

