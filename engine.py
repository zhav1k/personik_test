import pandas as pd
import numpy as np
import re
import pymorphy2
from razdel import tokenize
from navec import Navec
from pyaspeller import Word
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score
import argparse
#skip gram is best for semantics

def preprocess(text, morph, normalize = True):
    if normalize: text = transform_to_normal_form_([spellcheckword(tok.lower()) for tok in tokenize_sent(text)], morph)
    else: text = [spellcheckword(tok.lower()) for tok in tokenize_sent(text)]
    return text
    
def spellcheckword(word):
    check = Word(word)
    if check.correct == False:
        try:
            return check.variants[0]
        except IndexError:
            return word
    else:
        return word

def transform_to_normal_form_(list_of_words, morph):
    return [morph.parse(word)[0].normal_form for word in list_of_words]

def tokenize_sent(text):
    return [_.text for _ in tokenize(text)]

def prepare_keyword_vectors(keywords, w2v):
    vec = []
    for group in keywords:
        vec.append(np.sum([w2v[keyword] for keyword in group], axis=0))
    return np.matrix(vec)

def predict_label(vector_sentence, kw_matrix, w2v):
    st_matrix = np.matrix([w2v[word] if word in w2v else np.array([0]*300)for word in vector_sentence])
    scores = cosine_similarity(kw_matrix, st_matrix)
    scores = np.max(scores, axis=1)
    decision = np.argmax(scores)
    max_score = np.max(scores)
    if max_score > 0.24999:
        return decision
    else:
        return 3