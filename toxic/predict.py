import re
from flask import url_for
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize


stops=set(stopwords.words('english'))


def getGloveVec(word, vec, dims=300):
    vc = np.zeros(dims)
    try:
        vc = np.array(vec.loc[word])
    except:
        vc = np.zeros(dims)
    return vc


def getDocVec(sentence, vec, dims):
    tokens = word_tokenize(sentence)
    vecs = np.zeros(dims)
    for word in tokens:
        vecs += getGloveVec(word, vec, dims)
    vecs /= len(tokens)
    return vecs

def getGloveCorpus(dims=300):
    # Set path and load corpus
    path = "./data/embedings/" #url_for("static",filename="data/")
    filename = f'glove.6B.{dims}d.txt'
    f = open(path+filename, 'r', encoding='latin2')
    vec_txt = f.read()

    vec_data = {}
    words = vec_txt.split('\n')
    for word in words:
        vec = word.split()
        if len(vec) == dims+1:
            vec_data[vec[0]] = np.array([np.float16(x) for x in vec[1:]])
    vec = pd.DataFrame(vec_data, columns=None).transpose()
    return vec


def textPreprocess(text):
    cleanText = text.strip()
    cleanText = text.lower()
    cleanText = word_tokenize(cleanText)
    cleanText = [word for word in cleanText if word not in stops]
    cleanText = " ".join(cleanText)
    cleanText = cleanText.replace('\n'," ")
    cleanText = re.sub(r"(?:^|\W)utc(?:$|\W)",'',cleanText)
    cleanText = re.sub(r'http[s]*://[A-Za-z0-9:./?=]*','url',cleanText)
    cleanText = re.sub(r"[^a-z\s]",'',cleanText)
    cleanText = re.sub(r'[\s]+'," ",cleanText)
    return cleanText






def predict(text,VEC,model):

    lol = getDocVec(textPreprocess(text), VEC, 300)

    lol = np.reshape([lol],(1,1,300))

    prediction =  model.predict(lol)

    print(prediction)
    
    x = [int(i*100) for i in prediction[0] ]
    print(x)

    
    return x

