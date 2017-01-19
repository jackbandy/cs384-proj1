import nltk
from nltk import word_tokenize

hillary = word_tokenize(open('hillaryall.txt').read().decode('utf-8'))
hillarytext = nltk.Text(hillary)
sanders = word_tokenize(open('sandersall.txt').read().decode('utf-8'))
sanderstext = nltk.Text(sanders)
rubio = word_tokenize(open('rubioall.txt').read())
rubiotext = nltk.Text(rubio)
trump = word_tokenize(open('trumpall.txt').read().decode('utf-8'))
trumptext = nltk.Text(trump)
carson = word_tokenize(open('carsonall.txt').read().decode('utf-8'))
carsontext = nltk.Text(carson)
bush = word_tokenize(open('bushall.txt').read().decode('utf-8'))
bushtext = nltk.Text(bush)

alltexts = [hillarytext,sanderstext,rubiotext,trumptext,carsontext,bushtext]

hilllower = [x.lower() for x in hillarytext]
hillfreq = FreqDist(hilllower)
sanderslower = [x.lower() for x in sanderstext]
sandersfreq = FreqDist(sanderslower)
rubiolower = [x.lower() for x in rubiotext]
rubiofreq = FreqDist(rubiolower)
trumplower = [x.lower() for x in trumptext]
trumpfreq = FreqDist(trumplower)
carsonlower = [x.lower() for x in carsontext]
carsonfreq = FreqDist(carsonlower)
bushlower = [x.lower() for x in bushtext]
bushfreq = FreqDist(bushlower)

allfreqs = [hillfreq,sandersfreq,rubiofreq,trumpfreq,carsonfreq,bushfreq]

for txt in alltexts:
	len(set([x.lower() for x in txt]))
def lexdiv(text):
	return float(len(text)) / len(set([x.lower() for x in text])
for txt in alltexts:
	lexdiv(txt)

#To get other features, I used the same general for loop
for txt in alltexts:
	feature(txt)
