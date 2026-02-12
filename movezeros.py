num = [1, 0, 23, 0, 0, 6, 7, 0]

n = len(num)

for i in range(len(num)):
  if num[i]==0:
    num.remove(num[i])
    num.append(0)

print(num)