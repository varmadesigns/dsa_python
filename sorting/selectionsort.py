num = [5,3,6,3,6,7,7,3,11,2,6]

def selection(nums):
    n=len(num)
    for i in range(0,n):
        mini_ind=i
        for j in range(i+1,n):
            if nums[j]<nums[mini_ind]:
                mini_ind=j
        nums[i],nums[mini_ind]=nums[mini_ind],nums[i]
    print(nums)

selection(num)