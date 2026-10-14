# vaiablr scope = Where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in
#functions can't see what inside another function

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()