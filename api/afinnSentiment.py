import json
import re

text='hello are you okay?Are you happy.are you sad.happy happy'


with open('afinn111.json') as f:
    data = json.load(f)

words=re.split(r'[.,?\s]+', text)
#words = re.findall(r'\w+', text)

sentiment=0
for i in range(len(words)):
	if words[i] in data:
		sentiment=sentiment+int(data[words[i]])
		
print(sentiment)


