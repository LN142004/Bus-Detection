import torch

def load_model(weights_path="yolov5/runs/train/exp/weights/best.pt"):
    return torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)
