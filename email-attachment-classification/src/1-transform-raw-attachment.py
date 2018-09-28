
# coding: utf-8

# # Transform email attachment into document and label

# In[3]:


import os
import json
import subprocess
import textract

def readDocFile(filePath):
    readText = subprocess.Popen("antiword -m UTF-8.txt \"" + filePath + "\"", shell=True, stdout=subprocess.PIPE).stdout.read()
    return readText

path = '/notebooks/data/raw/'
folders = os.listdir(path)

documents = []
labels = []
fileNames = []

for folder in folders:
    directory = path + folder
    for root, directories, files in os.walk(directory):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            fileExtension = filePath.split('.')[-1]
      
            if fileExtension == 'pdf':
                try:
                    documents.append(textract.process(filePath, method='pdftotext'))
                    labels.append(folder)
                    fileNames.append(fileName)
                except:
                    print 'Cannot read .pdf file.'
                    pass
            elif fileExtension == 'docx':
                try:
                    documents.append(textract.process(filePath))
                    labels.append(folder)
                    fileNames.append(fileName)
                except:
                    print 'Cannot read .docx file.'
                    pass
            elif fileExtension == 'doc':
                try:
                    documents.append(readDocFile(path + folder + '/' + fileName))
                    labels.append(folder)
                    fileNames.append(fileName)
                except:
                    print 'Cannot read .doc file.'
                    pass

with open('/notebooks/data/documents.json', 'w') as outfile:
    json.dump(documents, outfile, indent=4)

with open('/notebooks/data/labels.json', 'w') as outfile:
    json.dump(labels, outfile, indent=4)

with open('/notebooks/data/fileNames.json', 'w') as outfile:
    json.dump(fileNames, outfile, indent=4)

