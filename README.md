# Bi-GRU Sequence Classifier (Keras 3)

A high-performance, deep learning sequential model architecture tailored for Natural Language Processing (NLP) text classification, sentiment analysis, and sequence-based feature extraction. Built using the modern **Keras 3** unified framework.

---

## 🚀 Architecture Overview

The model employs stacked **Bidirectional Gated Recurrent Units (Bi-GRU)** combined with aggressive regularization and specialized dimensional mapping to extract high-quality temporal configurations without suffering from vanishing gradients or severe overfitting.
Input [Shape: (None, 400)]
│
▼
Embedding Layer [Vocab: 30,000 | Output Dim: 64] (Zero Masking Enabled)
│
▼
Bidirectional GRU [Layer 1 | Units: 64 | Dropout: 0.4 | Recurrent Dropout: 0.3]
│
▼
Dropout Layer [Rate: 0.4]
│
▼
Bidirectional GRU [Layer 2 | Units: 32 | Dropout: 0.4 | Recurrent Dropout: 0.3]
│
▼
Dropout Layer [Rate: 0.4]
│
▼
Global Max Pooling 1D
│
▼
Dense Layer [Units: 32 | Activation: ReLU | L2 Regularization: 0.001]
│
▼
Batch Normalization
│
▼
Dropout Layer [Rate: 0.5]
│
▼
Dense Output [Units: 1 | Activation: Sigmoid (Binary Classification)]


---

## 🛠️ Model Configuration Breakdown

* **Input Specifications:** Expects an input matrix of shape `(batch_size, 400)`, representing sequence-padded text token indexes.
* **Embedding Matrix:** Outfitted with a vocabulary size of `30,000` mapped into a `64`-dimensional dense space. `mask_zero=True` ensures padding values do not disrupt temporal calculations.
* **Recurrent Regularization:** Variational dropout (`0.4`) and recurrent dropout (`0.3`) are compiled natively inside both GRU components. 
* **Stable Optimization Layers:** Features `L2` kernel regularization (`0.001`), standard `BatchNormalization`, and an anchor output dropout rate of `0.5` prior to final calculations.

---

## ⚙️ Compilation & Training Configurations

The model is configured with a low-variance optimizer profile optimized for sensitive structural classification routines:

| Parameter | Configuration |
| :--- | :--- |
| **Optimizer** | Adam |
| **Learning Rate** | $5.0 \times 10^{-4}$ (`0.0005`) |
| **Loss Function** | Binary Crossentropy |
| **Evaluation Metrics** | Accuracy, ROC-AUC, Precision, Recall |
| **DType Policy** | `float32` |

---

## 💻 Quick Start

### Prerequisites
Ensure you have the compatible library environments active:
```bash
pip install keras>=3.12.0 tensorflow
Loading the Model Architecture
You can instantiate this model directly within Keras using Python:

Python
import keras
from keras import layers
from keras import regularizers

def build_bi_gru_classifier():
    model = keras.Sequential([
        # Input and Embedding
        layers.Input(shape=(400,), dtype="float32", name="input_layer"),
        layers.Embedding(input_dim=30000, output_dim=64, mask_zero=True, name="embedding_1"),
        
        # First Bi-GRU Block
        layers.Bidirectional(
            layers.GRU(64, return_sequences=True, dropout=0.4, recurrent_dropout=0.3, reset_after=True),
            name="bidirectional_2"
        ),
        layers.Dropout(0.4, name="dropout_3"),
        
        # Second Bi-GRU Block
        layers.Bidirectional(
            layers.GRU(32, return_sequences=True, dropout=0.4, recurrent_dropout=0.3, reset_after=True),
            name="bidirectional_3"
        ),
        layers.Dropout(0.4, name="dropout_4"),
        
        # Pooling & Latent Feature Processing
        layers.GlobalMaxPooling1D(name="global_max_pooling1d_1"),
        layers.Dense(32, activation="relu", kernel_regularizer=regularizers.L2(0.001), name="dense_2"),
        layers.BatchNormalization(name="batch_normalization_1"),
        layers.Dropout(0.5, name="dropout_5"),
        
        # Classifier Output
        layers.Dense(1, activation="sigmoid", name="dense_3")
    ], name="sequential_1")
    
    # Compile exactly as specified in configuration metadata
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.0005),
        loss="binary_crossentropy",
        metrics=["accuracy", keras.metrics.AUC(name="auc"), "precision", "recall"]
    )
    return model

model = build_bi_gru_classifier()
model.summary()
💾 Metadata info
Keras Version Used: 3.12.3

Date Exported: 2026-07-10@23:21:05
