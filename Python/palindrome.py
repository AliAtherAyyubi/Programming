

word= str(input("Enter any word: "))

# str='hamza'
# print(len(str))
# print(str[4])
i=len(word)-1
convert=""
while i>=0:
    convert+=word[i]
    i=i-1

if convert==word:
    print("This word is a palindrome")
else:
    print("This word is not a Palindrome")