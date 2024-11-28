



stack=[]

def isEmpty():
        return len(stack)==0  

def push(data):
    stack.append(data)

def pop():
    if isEmpty()==False:
         stack.pop()
    else:
         print("Stack is empty Now")

def printStack():
    for i in stack:
        print(i)

push(1)
push(3)
push(13)
push(12)
push('ali')
printStack()

pop()
pop()
pop()
pop()
pop()
print("After pop")
printStack()