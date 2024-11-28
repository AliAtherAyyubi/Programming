
def secretKey(key):
    print(key)

    if(key<17):
        secretKey(secretKey(secretKey(key=key+1)))
    
    return key


secretKey(15)