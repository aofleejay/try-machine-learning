import json
import tnthai.segment as tn

with open('/notebooks/data/attachments.json', 'r') as file:
  attachments = json.load(file)
  segmented = []

  for attachment in attachments:
    content = attachment['content'].encode('utf-8')
    term = tn.UnsafeSegment(content)
    segmented.append(term[1][0])

with open('/notebooks/data/segments.json', 'w') as outfile:
  json.dump(segmented, outfile, indent=4)
  