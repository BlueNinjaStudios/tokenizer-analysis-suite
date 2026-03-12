import json
import os

data = {}

text = []

with open("BNE/bne_byteLevel_minipile_5_tokens_262144.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    for i, elem in enumerate(data["model"]["merges"]):
        if len(elem) > 48:
            text.append(f"Merge_num: {i} Tokens: {len(elem)} characters: {len(''.join(elem))}\n")
            text[-1] += "".join(elem) + "\n\n"

for i, elem in enumerate(text):
    text[i] = f"{i}: " + elem

with open("longest_merges_48.txt", "w", encoding="utf-8") as file:
    file.write("".join(text))

"""
for token in tokens:
    with open("data/BNE/bne_byteLevel_minipile_full_tokens_262144.json", "r") as file:
        data = json.load(file)
    vocab = len(data["model"]["vocab"])
    merges = len(data["model"]["merges"])
    data_file = data
    data_file["model"]["vocab"] = list(data["model"]["vocab"])[:token]
    data_file["model"]["merges"] = list(data["model"]["merges"])[:(merges-2**18+token)]
    with open("data/BNE/bne_byteLevel_minipile_full_tokens_262144.json".replace(str(2**18), str(token)), "w") as file:
        file.write(json.dumps(data_file))
"""


# Rename files for BNE_old_algo
"""
for file in os.listdir("data/BNE_old_algo"):
    os.rename("data/BNE_old_algo/" + file, "data/BNE_old_algo/" + file.replace("bne", "bne_old_algo"))
"""