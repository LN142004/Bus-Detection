import os

def train_model(data_yaml="custom.yaml", weights="yolov5s.pt"):
    os.system(f"python yolov5/train.py --img 640 --batch 4 --epochs 110 --data {data_yaml} --weights {weights} --cache")
