
# coding: utf-8

# # Vectorization

# ## TF-IDF

# In[1]:


import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

with open('/notebooks/data/word-sequences.json', 'r') as file:
    wordSequences = json.load(file)

vectorizer = TfidfVectorizer()
vectorizer = vectorizer.fit(wordSequences)

pickle.dump(vectorizer, open("/notebooks/src/vectorizer/tfidf.pickle", "wb"))

