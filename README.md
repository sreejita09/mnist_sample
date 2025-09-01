# MNIST Digit Classifier 🧠🔢

This is my first deep learning project using **TensorFlow**.  
It trains a simple neural network on the classic [MNIST dataset](http://yann.lecun.com/exdb/mnist/) of handwritten digits (0–9).

---

## 📌 Project Overview
- **Goal**: Classify handwritten digits (28×28 grayscale images).  
- **Dataset**: MNIST (60,000 training images + 10,000 test images).  
- **Model**: A fully connected neural network with:
  - Flatten layer (to convert 28×28 images into vectors)
  - Dense hidden layer with ReLU activation
  - Dense output layer with softmax activation (10 classes)
- **Optimizer**: Adam  
- **Loss**: Sparse Categorical Crossentropy  
- **Metrics**: Accuracy  

---

## 🚀 Results
- Training Accuracy: ~98%  
- Validation Accuracy: ~97–98%  
- Below is the training curve:

<img width="780" height="674" alt="image" src="https://github.com/user-attachments/assets/45f97018-32a7-4f40-92d4-050874842073" />


---

## 🛠️ Technologies Used
- Python  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  
