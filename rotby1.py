num = [1, 2, 23, 4, 5, 6, 7, 8]


k = int(input("Enter the number of rotations: "))

k = k % len(num)
if k != 0:
    num[:k], num[k:] = num[-k:], num[:-k]

print(num)
