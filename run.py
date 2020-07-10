# 
import numpy as np
import re
import pymorphy2
from razdel import tokenize
from navec import Navec
from pyaspeller import Word
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score
from engine import *
import config
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run topic prediction script")
    parser.add_argument("-m", "--message", type=str, help="Past your message to classify", default="мне нужно посетить врача")
    args = parser.parse_args()
    morph = pymorphy2.MorphAnalyzer()
    w2v = Navec.load(config.path)
    keyword_matrix = prepare_keyword_vectors(config.keywords, w2v)
    processed_text = preprocess(args.message, morph, config.normalized)
    print(config.inv_mapping[predict_label(processed_text, keyword_matrix, w2v)])