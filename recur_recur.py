def func(sum,i,n):
    if n==0:
        print(sum)
        return
    func(sum+i,i+1,n-1)

func(0,1,50)