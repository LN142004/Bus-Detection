import torch

def load_model(weights_path="best.pt"):
    return torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)
