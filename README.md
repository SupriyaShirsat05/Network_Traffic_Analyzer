# Network Traffic Analyzer
### ML-Based Network Traffic Classification and Attack Detection

A machine learning-based network traffic analyzer that classifies network traffic into normal traffic and selected flood attack categories using extracted packet-level features. The project uses a trained Scikit-learn model and a Flask API to provide predictions through a simple web interface.

## Overview

Network attacks such as SYN Flood, ACK Flood, and FIN Flood can generate abnormal traffic patterns and affect network availability. This project explores the use of machine learning to classify network traffic based on selected packet features.

The application accepts traffic feature values through a web interface, sends them to a Flask backend, and returns the predicted traffic category.

## Features

- Machine learning-based network traffic classification
- Detection of four configured traffic classes
- Flask REST API for model inference
- Web interface for entering packet features and viewing predictions
- Reusable trained model stored as `model.pkl`
- Jupyter notebooks for dataset exploration and model development
- Mininet topology script for network experimentation

## Traffic Classes

| Class ID | Predicted label |
|---:|---|
| 0 | Normal |
| 1 | SYN Flood |
| 2 | ACK Flood |
| 3 | FIN Flood |

**Note:** These are the categories configured in the application. Detection performance depends on the training data and model evaluation results.

## Technology Stack

- **Programming language:** Python
- **Machine learning:** Scikit-learn
- **Data processing:** Pandas, NumPy
- **Backend:** Flask
- **Model serialization:** Joblib
- **Frontend:** HTML, CSS, JavaScript
- **Network experimentation:** Mininet, Wireshark, packet captures
- **Development tools:** Jupyter Notebook, Git, GitHub

## Input Features

The model currently expects three features in this order:

| Feature | Description |
|---|---|
| `frame.time_relative` | Relative packet timestamp from the capture |
| `tcp.dstport` | TCP destination port |
| `frame.len` | Frame length in bytes |

The backend constructs a Pandas DataFrame using these column names before passing the values to the trained model.

**Important:** Predictions are based on these three features only. The application is a prototype for traffic classification and should not be treated as a production-grade intrusion detection or prevention system.

## Project Structure

```text
Network_Traffic_Analyzer/
├── app.py
├── predict.py
├── model.pkl
├── requirements.txt
├── final_multiclass_dataset.csv
├── Main.ipynb
├── balanced_tcp_dataset.ipynb
├── Topology/
│   └── topo.py
├── templates/
│   └── index.html
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SupriyaShirsat05/Network_Traffic_Analyzer.git
cd Network_Traffic_Analyzer
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the environment's Python executable directly instead.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure that the dependencies are compatible with the environment used to create `model.pkl`. The model was developed with Scikit-learn 1.7.2.

### 4. Run the Flask application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

Enter the three traffic feature values and select **Analyze Traffic** to view the model's prediction.

## API Documentation

### `GET /`

Serves the web interface.

### `POST /predict`

Accepts three numerical traffic features as a JSON array.

**Example request:**

```json
{
  "features": [0.619518, 16852.0, 54]
}
```

The values represent:

1. Relative frame time
2. TCP destination port
3. Frame length

**Example response:**

```json
{
  "class_id": 0,
  "label": "Normal"
}
```

The predicted label depends on the loaded model and the input values; the example response is illustrative.

## Model Workflow

1. Collect or obtain network traffic data.
2. Extract relevant packet-level features.
3. Prepare the dataset for model development.
4. Train and save the classification model.
5. Load the serialized model in the Flask backend.
6. Receive input features from the web interface.
7. Generate and return the predicted traffic category.

## Network Experimentation

The repository includes a Mininet topology script under `Topology/`. Mininet and packet-analysis tools can be used in a suitable Linux environment to support controlled network traffic experiments.

The packet-capture files and larger intermediate datasets are excluded from the repository to keep the codebase lightweight. Obtain or regenerate any required experimental data separately.

## Limitations

- The model uses only three input features.
- Predictions depend on the quality and representativeness of the training data.
- The current interface accepts manually entered feature values rather than automatically capturing live network traffic.
- No production-grade authentication, rate limiting, or intrusion-prevention mechanism is implemented.
- Model accuracy and generalization must be established through documented evaluation on independent test data.

## Future Improvements

- Add automated packet capture and feature extraction.
- Evaluate additional machine learning algorithms.
- Report precision, recall, F1-score, confusion matrix, and per-class
