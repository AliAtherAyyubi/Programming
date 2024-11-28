

# program to find factorial of the given number

def factorial(n):
    result=1
    if n>0:
        while n>0:
            result= result*n
            n=n-1
        print("factorial: ",result)
    else:
        print('Number is not valid')


number= int(input("Enter any Number: "))
# print(number)
factorial(number)
        