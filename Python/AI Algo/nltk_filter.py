
        # program to filter a sentence by removing stopwords

import nltk
from nltk.corpus import stopwords

sentence='how to find account setting in windows 10'

# // to convert into tokens a sentence
tokens= nltk.word_tokenize(sentence)

# to convert into keywords or remove stopwords //

Stopwords=set(stopwords.words('english'))
filter=[]
for word in tokens:
    if word not in Stopwords:
        filter.append(word)

print('Filtered Sentence: ',filter)
# print(tokenize)