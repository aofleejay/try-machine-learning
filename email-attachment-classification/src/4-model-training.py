
# coding: utf-8

# # Model Training

# In[ ]:


import json
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, recall_score, precision_score, classification_report, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

with open('/notebooks/data/documents.json', 'r') as file:
    documents = json.load(file)

with open('/notebooks/data/labels.json', 'r') as file:
    labels = json.load(file)

vectorizer = pickle.load(open("/notebooks/src/vectorizers/tfidf.pickle", 'rb'))

Xtrain = vectorizer.transform(documents).toarray()
Ytrain = np.asarray(labels)


# ## MultinomialNB

# In[ ]:


modelMultinomialNB = MultinomialNB(alpha=0.01).fit(Xtrain, Ytrain)
joblib.dump(modelMultinomialNB, '/notebooks/src/models/MultinomialNB.pkl')

YMultinomialNBPredict = modelMultinomialNB.predict(Xtrain)

print confusion_matrix(Ytrain, YMultinomialNBPredict, labels=list(set(Ytrain)))
print classification_report(Ytrain, YMultinomialNBPredict)
# print cross_val_score(modelMultinomialNB, Xtrain, Ytrain, cv=10)

