import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.metrics import confusion_matrix, recall_score, precision_score, classification_report, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

with open('/notebooks/data/x.json', 'r') as file:
    x = json.load(file)

with open('/notebooks/data/y.json', 'r') as file:
    y = json.load(file)
    
vectorizer = TfidfVectorizer()
Xtrain = vectorizer.fit_transform(x).toarray()
Ytrain = np.asarray(y)

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
