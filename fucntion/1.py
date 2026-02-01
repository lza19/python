z = 0
def reg(x, y):
    z = x *y
    print("reg : ", z)
    return z

a = reg(3, 4)
print("global a : ", a)

def pow(x,y):
    z = x ** y
    return z

b = int(input("Enter base: "))
c = int(input("Enter exponent: "))
d = pow(b, c)
print(b,'**',c,'=',d)


klist = [1, 2, 3, 4, 5]
a = max(klist)
print("max value in klist : ", a)