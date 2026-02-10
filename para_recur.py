n=4
x=15

def func(n,x):
    if n==0:
        return x
    print(x)
    return func(n-1,x)

func(n,x)