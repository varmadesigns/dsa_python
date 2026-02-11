s=input("enter a string:")

def paliandrome(s):
    return s==s[::-1]

if paliandrome(s):
    print("paliandrome")
else:    print("not paliandrome")