def func(n,x):
    if n==0:
        return x
    print(x)
    return func(n-1,x+1)

func(5,1)
