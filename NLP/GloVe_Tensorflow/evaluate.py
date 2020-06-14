# -*- coding: utf-8 -*-
"""eval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pFfVgzJrKZNxFqCTFYbz796Xb77Skzsg
"""

import argparse
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def are_Similar(word1, word2, model):

    word1_embed = model.embedding_for(word1)
    word2_embed = model.embedding_for(word2)

    similar = np.dot(word1_embed,word2_embed.T)/np.sqrt((np.abs(np.dot(word1_embed,word1_embed.T))*np.abs(np.dot(word2_embed,word2_embed.T))))
    return similar

def get_ClosestWords(target, model, num_required_words=10):
    top_words = list()
    for word in model.words:
        top_words.append([word, are_Similar(target, word, model)])
    top_words.sort(key = lambda x: x[1],reverse=True)
    return top_words[:num_required_words]   
  
def analogy(word1, word2, word3, model, num_required_words=10):
    vocab = model.words
    word4_embed = model.embedding_for(word1) - model.embedding_for(word2) + model.embedding_for(word3)

    top_words = list()
    for word in vocab:
        word_embed = model.embedding_for(word)
        similar = np.dot(word_embed,word4_embed.T)/np.sqrt((np.abs(np.dot(word_embed,word_embed.T))*np.abs(np.dot(word4_embed,word4_embed.T))))
        top_words.append([word, similar])
    top_words.sort(key = lambda x: x[1],reverse=True)
    return top_words[:num_required_words]