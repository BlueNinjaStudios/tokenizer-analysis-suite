from tokenizers import Tokenizer
from tokenizers.models import BNE
from tokenizers.trainers import BneTrainer
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.decoders import ByteLevel
import datasets

# Load dataset
dataset = datasets.load_dataset("JeanKaddour/minipile", split="test")

# Load tokenizer
tokenizerBNE = Tokenizer.from_file("source_data/minipile_full/data/BNE/bne_byteLevel_minipile_full_tokens_8192.json")
tokenizerBPE = Tokenizer.from_file("source_data/minipile_full/data/BPE/bpe_byteLevel_minipile_full_tokens_8192.json")

tokenizerBNE.decoder = ByteLevel()
tokenizerBPE.decoder = ByteLevel()

text = dataset["text"][1]


print(f"orig:       {text}")
print("---- BNE ----")
print(f"encoded:    {[tokenizerBNE.decode([id]) for id in tokenizerBNE.encode(text).ids][:100]}")
print("---- BPE ----")
print(f"encoded:    {[tokenizerBPE.decode([id]) for id in tokenizerBPE.encode(text).ids][:100]}")