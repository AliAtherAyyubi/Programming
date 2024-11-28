

import nltk
from nltk.stem import PorterStemmer

sentence="The crew of the USS Discovery discovered many discoveries.Discovering is what explorers do."

stemmer=PorterStemmer();

words=nltk.word_tokenize(sentence)

stemmed_words=[]

for i in words:
    stemmed_words.append(stemmer.stem(i))

print(stemmed_words)