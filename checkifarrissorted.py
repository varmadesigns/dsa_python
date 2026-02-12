num = [1,2,3,4,5,6,7,8]

n= len(num)

for i in range(0,n-1):
    if num[i]>num[i+1]:
        print("not sorted")
        break
else:
    print("sorted")

num=num[::-1]

print(num)
        