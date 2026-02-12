num = [1,1,1,2,2,3,5,22,3,5,5,6,6,6]

n=len(num)

freq_map={}

for i in range(0,n):
    freq_map[num[i]]=0

j=0
for k in freq_map:
    num[j]=k
    j+=1

print(num[:j])