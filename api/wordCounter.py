import re

def wordCounter(text):
	words=re.split(r'[.,?\s]+', text)
	wordCounter={}
	for i in words:
		if i not in wordCounter:
			wordCounter[i]=1
		else:
			wordCounter[i]+=1
	return wordCounter