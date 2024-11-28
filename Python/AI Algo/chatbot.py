
import string

print('Choose questions from below list:')
print("hi")
print("how are you?")
print("Are you working?")
print("What is your name?")
print("What did you do yesterday?")
print('Quit')



while True:
    q= str(input('Enter your question: '))
    # nq=q.translate(str.maketrans('','',string.punctuation))
    print(nq)
    q=q.lower()
    # print(q)
    if q in ['hi','hello']:
        print('Hello\nHow may I help you!')
    elif q in ['how are you?','how do you do?']:
        print('I am good what about you')
        ans=input("")
        print('Good to hear sir!')
    elif q in ['how are you?']:
        print('I am good what about you')
    elif q in ['what is your work','are you doing any job?']:
        print('I am working in GCU')
    elif q in ['what is your name']:
        print('My name is Emilia.What is your name?')
        ans=input("")
        print('Nice to meet you ',ans.upper())
    elif q in ['quit']:
        break
    else:
        print('I do not understand what you said! ')
        
