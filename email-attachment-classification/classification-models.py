import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.metrics import confusion_matrix, recall_score, precision_score, classification_report, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import pickle

with open('/notebooks/data/contents.json', 'r') as file:
    contents = json.load(file)

with open('/notebooks/data/labels.json', 'r') as file:
    labels = json.load(file)

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit(contents)

pickle.dump(tfidf, open("tfidf.pickle", "wb"))
tfidf = pickle.load(open("tfidf.pickle", 'rb'))

Xtrain = tfidf.transform(contents).toarray()
Ytrain = np.asarray(labels)

# MultinomialNB

modelMultinomialNB = MultinomialNB(alpha=0.01).fit(Xtrain, Ytrain)
joblib.dump(modelMultinomialNB, 'MultinomialNB.pkl')

YmodelMultinomialNBPredict = modelMultinomialNB.predict(Xtrain)

print confusion_matrix(Ytrain, YmodelMultinomialNBPredict, labels=list(set(Ytrain)))
print classification_report(Ytrain, YmodelMultinomialNBPredict)
# print cross_val_score(modelMultinomialNB, Xtrain, Ytrain, cv=10)

# # GaussianNB

# modelGaussianNB = GaussianNB().fit(Xtrain, Ytrain)
# joblib.dump(modelGaussianNB, 'GaussianNB.pkl')

# YmodelGaussianNBPredict = modelGaussianNB.predict(Xtrain)

# print confusion_matrix(Ytrain, YmodelGaussianNBPredict, labels=list(set(Ytrain)))
# print classification_report(Ytrain, YmodelGaussianNBPredict)
# print cross_val_score(modelGaussianNB, Xtrain, Ytrain, cv=10)

# # BernoulliNB

# modelBernoulliNB = BernoulliNB(alpha=0.01).fit(Xtrain, Ytrain)
# joblib.dump(modelBernoulliNB, 'BernoulliNB.pkl')

# YmodelBernoulliNBPredict = modelBernoulliNB.predict(Xtrain)

# print confusion_matrix(Ytrain, YmodelBernoulliNBPredict, labels=list(set(Ytrain)))
# print classification_report(Ytrain, YmodelBernoulliNBPredict)
# print cross_val_score(modelBernoulliNB, Xtrain, Ytrain, cv=10)
