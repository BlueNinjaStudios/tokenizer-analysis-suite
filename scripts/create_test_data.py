import datasets
import json
import os

# Load dataset
dataset = list(datasets.load_dataset("JeanKaddour/minipile", split="test"))

with open("source_data/language/minipile_10_3.json", "w") as file:
    file.write(json.dumps(dataset))