import os, json, subprocess
import textract

def readDocByFileName(filename):
  readtext = subprocess.Popen("antiword -m UTF-8.txt \"" + filename + "\"", shell=True, stdout=subprocess.PIPE).stdout.read()
  return readtext

path = '/notebooks/data/raw/'
folders = os.listdir(path)

attachments = []
for folder in folders:
  directory = path + folder
  for root, directories, files in os.walk(directory):
    for fileName in files:
      filePath = os.path.join(root, fileName)
      fileExtension = filePath.split('.')[-1]
      
      if fileExtension == 'pdf':
        try:
          attachments.append({ "name": fileName, "type": folder, "content": textract.process(filePath, method='pdftotext') })
        except:
          print 'Cannot read .PDF file.'
          pass
      elif fileExtension == 'docx':
        attachments.append({ "name": fileName, "type": folder, "content": textract.process(filePath) })
      elif fileExtension == 'doc':
        attachments.append({ "name": fileName, "type": folder, "content": readDocByFileName(path + folder + '/' + fileName) })

with open('/notebooks/data/attachments.json', 'w') as outfile:
  json.dump(attachments, outfile, indent=4)
