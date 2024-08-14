from transformers import pipeline
from PIL import Image
import requests
import torch


device =  torch.device('cuda' if torch.cuda.is_available() else "cpu")
print("device", device)
# load pipe
image_classifier = pipeline(task="zero-shot-image-classification", model="google/siglip-base-patch16-224", device = device)

# load image
url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

# inference
candidate_labels = ["2 cats", "a plane", "a remote"]
outputs = image_classifier(image, candidate_labels=candidate_labels)
outputs = [{"score": round(output["score"], 4), "label": output["label"] } for output in outputs]
print(outputs)