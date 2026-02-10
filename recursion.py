
count = 0

def func():
    global count

    if count == 5:
        return

    print("Hello")
    count += 1
    func()


func()