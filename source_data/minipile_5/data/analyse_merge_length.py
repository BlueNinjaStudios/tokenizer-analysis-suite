import json
import os
import matplotlib.pyplot as plt

scale = [str(i) for i in range(20)]
vals = [0 for i in range(20)]

with open("BNE/bne_byteLevel_minipile_5_tokens_262144.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    for i, elem in enumerate(data["model"]["merges"]):
        if len(elem) < 20:
            vals[len(elem)] += 1

fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200)

fig.suptitle('Merge lengths BNE$_\infty$ trained on Minipile 5% Slice', fontsize=16)

ax.plot(scale, vals)

plt.savefig("merge_lengths_2.png")