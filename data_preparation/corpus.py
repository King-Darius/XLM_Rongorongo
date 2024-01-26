import pandas as pd
import os

from .encoding.encoding import encode_texts

# Original corpus transliterated in Barthel's system
CORPUS = {}
CORPUS_NO_BREAKS = {}   # Same as CORPUS but without line breaks

for text in os.listdir(os.path.join(os.path.dirname(__file__), "raw_texts")):
    CORPUS[text[:-4]] = {}
    CORPUS_NO_BREAKS[text[:-4]] = {'all_lines': ''}
    labels = pd.read_csv(os.path.join(os.path.dirname(__file__), f"raw_texts/{text}"), header=None).values[:,0]
    lines = pd.read_csv(os.path.join(os.path.dirname(__file__), f"raw_texts/{text}"), header=None).values[:,1]
    for i,line in enumerate(lines):
        CORPUS[text[:-4]][labels[i]] = line
        CORPUS_NO_BREAKS[text[:-4]]['all_lines'] += line
        if i < len(lines)-1:
            CORPUS_NO_BREAKS[text[:-4]]['all_lines'] += '-'

# The corpus re-encoded in Horley's system
CORPUS_HORLEY = encode_texts(CORPUS)
CORPUS_HORLEY_NO_BREAKS = encode_texts(CORPUS_NO_BREAKS)
