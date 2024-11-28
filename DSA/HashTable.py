

hashTable= [[],]*10

def hashFunction(key):
    size= 10
    return key % size

# to Avoid collission use following function
# def linearProbing(index):
#     for i in range(1,10):
#         index= hashFunction(index+i)
#         if hashTable[index]!=None:
#             index= index+i

#     return index
        
        #  Inserting Data
def insertData(key,data):
    index= hashFunction(key)
    # if(hashTable[index]==None):
    hashTable[index]=[key,data]
    # else:
    #     index=linearProbing(index)
    #     hashTable[index]=[key,data]


insertData(123,'Apple')
# insertData(123,'App')
insertData(250,'Mnago')
insertData(12,'lahore')

print(hashTable)


