# SmartDigit – Handwriting Recognition

**Turn handwritten digits into digital predictions! 🖊️➡️🔢**

SmartDigit is a **simple yet powerful neural network** that recognizes handwritten numbers (0–9) using the **MNIST dataset**.  
Perfect for learning **how neural networks work in image classification**.

---

## 🚀 What We Did

- Loaded and preprocessed MNIST images  
- Built a **basic ANN** with 1 hidden layer (128 neurons)  
- Trained the model for 5 epochs  
- Evaluated on test data (~97% accuracy)  
- Visualized first 10 predictions in a clean, student-style manner  

---

## 📂 Project Structure

Handwriting-MNIST/
├── .venv/ # Virtual environment
├── data/ # MNIST dataset (optional)
├── notebooks/ # Jupyter notebook experiments
│ └── MNIST_ANN.ipynb
├── src/ # Python code
│ ├── model.py
│ ├── train.py
│ └── utils.py
├── .gitignore
├── requirements.txt
└── README.md



---

## 🎯 How to Run

1. Activate virtual environment:

- Windows: `.venv\Scripts\activate`  
- Mac/Linux: `source .venv/bin/activate`

2. Install dependencies:

```bash
pip install -r requirements.txt
Run the main script:


python src/train.py
Model trains, evaluates, and visualizes predictions automatically.

💡 Why It’s Cool
~97% test accuracy with a simple ANN

Easy to understand and modify

Perfect starting point for deep learning beginners

Can be extended to CNNs for even higher accuracy

📊 Sample Output
Predictions for first 10 test images:

Each image shows what the model predicts

Visual, clean, and beginner-friendly

⚡ Quick Takeaway
This project shows that even a simple neural network can learn to recognize handwritten digits effectively.
A great foundation for diving deeper into AI and computer vision!

