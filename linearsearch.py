num=[1,2,4,5,5,.233,12,42,34,24]

n=len(num)

dig = int(input("enter a number: "))

for i in range(0,n):
    if dig==num[i]:
        print("number in index", i)
        
else:
    print("number not found")
