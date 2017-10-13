#%% Sample: Gutenberg's Bible
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])
    
#%% WordNet
#==============================================================================
# WordNet is a lexical database for the English language, 
# which was created by Princeton, and is part of the NLTK corpus.
#==============================================================================
from nltk.corpus import wordnet

syns = wordnet.synsets("program")   # Work with synonyms (synset) of the word "program"
#print(syns)
#print(syns[0].name())
#print(syns[0].lemmas()[0].name())
#print(syns[0].definition())
#print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#==============================================================================
print('*** Similarities ***')
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print('{:.3%}'.format(w1.wup_similarity(w2)))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print('{:.2%}'.format(w1.wup_similarity(w2)))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cactus.n.01')
print('{:.1%}'.format(w1.wup_similarity(w2)))