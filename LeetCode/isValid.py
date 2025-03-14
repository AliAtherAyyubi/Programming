
def isValid(s):
    stack=[]
    for i in range(len(s)):
        if s[i] in ['(','{','[']:
            stack.append(s[i])            
        elif s[i] in [')','}',']']:
            if s[i]==')' and stack[len(stack)-1]=='(':
                stack.pop()
            elif s[i]=='}' and stack[len(stack)-1]=='{':
                stack.pop()
            elif s[i]==']' and stack[len(stack)-1]=='[':
                stack.pop()
            if len(stack)==0 and i==len(s)-1:
                return True
    return False       

is_valid=isValid('(]')

print(is_valid)