nums = [5,2,4,2,8,5,3,7,3,6,7]

n=len(nums)
 
hash_map={}

target = 10

for i in range(0,n-1):
    remaining = target - nums[i]
    if remaining in hash_map:
        print([hash_map[remaining],i])
        break
    hash_map[nums[i]]=i
