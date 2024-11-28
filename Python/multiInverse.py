

## Function to calculate Multiplicative Inverse of a given number //


def multiInverse(n,modular):
    ## x is number 
    x=1
    multiInverse=0
    while(True):
        x+=1
        if ((n*x)%modular==1):
            return x
        elif(x>200):
            return 0

n=12
modular=26
multiInverseNumber=multiInverse(n,modular)
if(multiInverseNumber==0):
    print('Multiplicative Inverse doesn\'t exist')
else:
    print("Multiplicative Inverse: ",multiInverseNumber)