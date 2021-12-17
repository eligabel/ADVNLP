import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk import ngrams
from sklearn.feature_extraction.text import CountVectorizer

def openTxt(file):
	f = open(file, "r")
	extText = f.readline()
	f.close()
	return extText

def trigMaker(file):
	vectorizer = CountVectorizer()
	x = vectorizer.fit_transform(file)
	y = vectorizer.get_feature_names_out()
	vectorizer2 = CountVectorizer(analyzer='char', ngram_range=(3, 3),max_features=10000)
	x2 = vectorizer2.fit_transform(file)
	y2 = vectorizer2.get_feature_names_out()

	return y2

print(trigMaker("a2-train.py")
print(trigMaker("a2-test.py")


