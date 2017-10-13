import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

#%% Chunking

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}""" #Use triple quotes in separating on multiple lines
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)
            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()

#%% Chinking
# Chinking is a lot like chunking, it is basically a way for you to remove a chunk from a chunk.
# The chunk that you remove from your chunk is your chink.
# The code is very similar, you just denote the chink, after the chunk, with }{ instead of the chunk's {}.

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<.*>+}                  
                                    }<VB.?|IN|DT|TO>+{"""         #Everything apart from VB.?|IN|DT|TO 

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()

#%% Named entities
# One of the most major forms of chunking in natural language processing is called "Named Entity Recognition."
# The idea is to have the machine immediately be able to pull out "entities" like people, places, things, 
# locations, monetary figures, and more.

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True) # Binary --> remove subcategory in name entities
            namedEnt.draw()
    except Exception as e:
        print(str(e))


process_content()