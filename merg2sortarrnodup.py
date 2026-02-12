num1 = [100, 50, 200, 1, 300, 25, 175]
num2 = [75, 250, 150, 2, 400, 10]

# Approach 1: Using Set (HashMap)
unique_set = set()

# Add all elements from num1
for num in num1:
    unique_set.add(num)

# Add all elements from num2
for num in num2:
    unique_set.add(num)

# Convert to sorted list
print("Result:", unique_set)