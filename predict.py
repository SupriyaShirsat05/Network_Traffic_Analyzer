import joblib
import numpy as np
import pandas as pd

model = joblib.load("model.pkl")

labels = {
    0: "Normal",
    1: "SYN Flood",
    2: "ACK Flood",
    3: "FIN Flood"
}

columns = ['frame.time_relative', 'tcp.dstport', 'frame.len']

def predict(features):
    df = pd.DataFrame([features], columns=columns)
    pred = model.predict(df)[0]
    return labels[int(pred)]

print(predict([0.619518, 16852.0, 54]))