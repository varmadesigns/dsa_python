num = [2,3,6,5,4,7,8,9,10]

n=len(num)

for i in num:
    if i not in num:
        print(i,"is the number")
else:
    print("error")