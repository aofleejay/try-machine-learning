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

clftextfile = {
    'MultinomialNB': MultinomialNB(alpha=0.01),
    'GaussianNB': GaussianNB(),
    'BernoulliNB': BernoulliNB(alpha=0.01) ,
}

# modelMultinomialNB = clftextfile["MultinomialNB"]
# # YmodelMultinomialNBPredict = modelMultinomialNB.fit(Xtrain, Ytrain).predict(Xtrain)
# joblib.dump(modelMultinomialNB.fit(Xtrain, Ytrain), 'modelMultinomialNB.pkl') 

# modelGaussianNB = clftextfile["GaussianNB"]
# YmodelGaussianNBPredict = modelGaussianNB.fit(Xtrain, Ytrain).predict(Xtrain)
# joblib.dump(modelGaussianNB.fit(Xtrain, Ytrain), 'modelGaussianNB.pkl') 

# modelBernoulliNB = clftextfile["BernoulliNB"]
# # YmodelBernoulliNBPredict = modelBernoulliNB.fit(Xtrain, Ytrain).predict(Xtrain)
# joblib.dump(modelBernoulliNB.fit(Xtrain, Ytrain), 'modelBernoulliNB.pkl') 

# print confusion_matrix(Ytrain, YmodelMultinomialNBPredict, labels=list(set(Ytrain)))
# print confusion_matrix(Ytrain, YmodelGaussianNBPredict, labels=list(set(Ytrain)))
# print confusion_matrix(Ytrain, YmodelBernoulliNBPredict, labels=list(set(Ytrain)))

# print classification_report(Ytrain, YmodelMultinomialNBPredict)
# print classification_report(Ytrain, YmodelGaussianNBPredict)
# print classification_report(Ytrain, YmodelBernoulliNBPredict)

# print cross_val_score(modelMultinomialNB, Xtrain, Ytrain, cv=10)
# print cross_val_score(modelGaussianNB, Xtrain, Ytrain, cv=10)
# print cross_val_score(modelBernoulliNB, Xtrain, Ytrain, cv=10)