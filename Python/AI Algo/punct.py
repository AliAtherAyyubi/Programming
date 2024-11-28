# punctaution checking in  a sentence

punctaution="[]/><$%#@!(){}*/-+#`~\|"

sentence="Hello@ I am a$ student of % Gcu[]{}+/ Lahore# "

sentence2=str(input("Enter your sentence: "))

no_punc=""

for i in sentence2:
    if i not in punctaution:
        no_punc=no_punc+i

print("Sentence with punctuation: \n"+no_punc)