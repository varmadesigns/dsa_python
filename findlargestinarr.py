num = [5, 3, 6, 3, 6, 7, 7, 3, 11, 2, 6]

largest = num[0]
# largest = float("-inf")

n=len(num)

for i in range(0,n):
    largest = max(largest,num[i])

print(largest)