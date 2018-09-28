# File Classification
File classification (pdf, doc and docx extension) using machine learning.

## Getting Started
Place your own raw files into `'data/raw'` folder (see folder structure section below). 
```
$ docker-compose up
$ docker exec -it [container id] bash
$ pip install tnthai
$ pip install textract
```

## Folder Structure
```
email-attachment-classification
├── data                     (Raw data `must` be place in `raw` folder.)
│   ├── raw                  (Contain raw data in pdf, doc and docx format.)
│   │   ├── folder1          (Folder name must be label eg. news, sport.)
│   │   │   ├── file1.pdf
│   │   │   ├── file2.doc
│   │   │   ├── file3.docx
│   │   └── folder2
│   │       └── file4.pdf
│   ├── documents.json       (Contain array of documents string.)
│   ├── fileNames.json       (Contain array of file name for debug.)
│   ├── labels.json          (Contain array of labels.)
│   └── word-sequences.json  (Pre-processed documents to use in vectorizer.)
├── src
│   ├── models               (Contain model files.)
│   ├── vectorizers          (Contain vectorizer files.)
│   ├── 1-step-one.ipynb
│   ├── 1-step-one.py
│   ├── 2-step-two.ipynb
│   └── 2-step-two.py
└── docker-compose.yml
```
