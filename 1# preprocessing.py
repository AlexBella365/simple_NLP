#%% TOKENIZING
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "This is a sample sentence, showing off the stop words filtration."
word_tokens = word_tokenize(example)

stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(word_tokens)
print(filtered_sentence)

#%% STEMMING
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
    
#%% POS (Part Of Speech) TAGGING
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text) #Pretrained tokenizer, can be retrained
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))

process_content()

#%% Lemmatizing 
# Similar to stemming BUT the end result is an actual exisitng word

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos="a"))  # Force it as an adjective
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("ran",'v'))          # Force it as a verb