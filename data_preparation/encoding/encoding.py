import os
import pandas as pd
import re


encoding_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'horley_encoding.csv'))
horley_encoding = dict(zip(encoding_df['Barthel'], encoding_df['Horley']))


def clean_glyph(glyph):
    """
    Splits a ligatured glyph into its components and removes all non-glyph characters.
    """
    glyphs = re.sub("[bcdeghijkostxy!*?()\[\]]", "", glyph.lower()).split('.')

    clean_glyphs = []

    # Handle correct reading order of glyphs from bottom up
    for gl in glyphs:
        if ':' in gl:
            clean_glyphs += gl.split(':')[::-1]
        else:
            clean_glyphs.append(gl)
    return [gl.lstrip('0') for gl in clean_glyphs]


def encode_glyph(glyph, encoding=horley_encoding):
    """
    Encodes a glyph from Barthel's system into a simplified encoding meant to handle
    fused glyphs and allographs (the default being Paul Horley's proposal).
    """
    clean_glyphs = clean_glyph(glyph)
    encoded = []
    for clean_gl in clean_glyphs:
        if clean_gl in encoding:
            encoded.append(encoding[clean_gl])
        else:
            # If the glyph is not in the encoding, let's check
            # for it without any alphabetic modifiers.
            num = re.sub("[a-z]", "", clean_gl)
            if num in encoding:
                res = encoding[num]
                encoded.append(res)
            else:
                if clean_gl:
                    encoded.append(clean_gl)
                else:
                    encoded.append('?')
    return ' '.join(encoded).replace('.', ' ')  # quick fix for the dot


def encode_line(line, encoding=horley_encoding):
    """
    Encodes a line of text from Barthel's system into a simplified encoding.
    """
    glyphs = line.split("-") # assume glyphs are separated by a dash
    return " ".join([encode_glyph(glyph, encoding) for glyph in glyphs])


def encode_texts(texts, encoding=horley_encoding):
    """
    Encodes the entire corpus of texts from Barthel's system into a simplified encoding.
    The corpus is assumed to be a dictionary of dictionaries, where the first key is the
    text identifier and the second key is the line identifier.
    """
    encoded_texts = {}
    for text_id in texts:
        encoded_texts[text_id] = {}
        for line_id in texts[text_id]:
            encoded_texts[text_id][line_id] = encode_line(texts[text_id][line_id], encoding)
    return encoded_texts
