import json

with open('/notebooks/data/segments.json', 'r') as file:
    segments = json.load(file)

with open('/notebooks/data/attachments.json', 'r') as file:
    attachments = json.load(file)

contents = []
labels = []
for words in segments:
    contents.append(" ".join(words))

for attachment in attachments:
    labels.append(attachment["type"])

with open('/notebooks/data/contents.json', 'w') as outfile:
    json.dump(contents, outfile, indent=4)

with open('/notebooks/data/labels.json', 'w') as outfile:
    json.dump(labels, outfile, indent=4)
