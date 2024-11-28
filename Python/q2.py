
import nltk
from nltk.corpus import stopwords


passage= 'Atoms of radioactive elements can split. According to Albert Einstein, mass and energy are interchangeable under certain circumstances. When atoms split, the process is called nuclear fission.'

# to convert into tokens
tokenize= nltk.word_tokenize(passage)

stop_word= set(stopwords.words('english'))

filter=[]

# loop to check stopwords
for word in tokenize:
    if word not in stop_word:
        filter.append(word)

print(filter)
