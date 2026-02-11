array = [5,2,2,4,6,7,8,2,1,3]
array2 = [5,2,2,4,6,7,8,2,1,3]
array3 = [5,2,2,4,6,7,8,2,1,3]



array.reverse()
array2 = array2[::-1]

print(array)
print(array2)

def reverse_array(arr, start, end):
    if start >= end:
        print (arr)
        return
    
    arr[start],arr[end]=arr[end],arr[start]

    reverse_array(arr,start+1,end-1)

reverse_array(array3,0,len(array3)-1)