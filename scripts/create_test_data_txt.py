import datasets
import json
import os

# Load dataset
dataset = datasets.load_dataset("JeanKaddour/minipile", split="test")

with open("source_data/language/minipile_10_2.txt", "w") as file:
    for row in dataset:
        file.write(row["text"].replace("\n\n", "\n"))