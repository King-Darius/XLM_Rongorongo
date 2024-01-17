import pandas as pd
import os

from .encoding.encoding import encode_texts

# Original corpus transliterated in Barthel's system
CORPUS = {}

for text in os.listdir(os.path.join(os.path.dirname(__file__), "raw_texts")):
    CORPUS[text[:-4]] = {}
    labels = pd.read_csv(os.path.join(os.path.dirname(__file__), f"raw_texts/{text}"), header=None).values[:,0]
    lines = pd.read_csv(os.path.join(os.path.dirname(__file__), f"raw_texts/{text}"), header=None).values[:,1]
    for i,line in enumerate(lines):
        CORPUS[text[:-4]][labels[i]] = line

# The corpus re-encoded in Horley's system
CORPUS_HORLEY = encode_texts(CORPUS)
