def GCD(x,y):
    if x > y:
        return False
    if x%y == 0:
        return y
    else:
        result = 1
        for i in range(int(y/2)):
            if x%(i+1) == 0 and y%(i+1) ==0:
                result = i+1
        return result
def LCM(x,y):
    if x > y:
        return False
    if x%y == 0:
        return x
    else:
        result = x*y
        for i in range(x*y,x,-1):
            if i%x==0 and i%y==0:
                result = i
        return result
def Sum3(x,y,z):
    if x==y or y==z or x==z:
        return 0
    else:
        return x+y+z
