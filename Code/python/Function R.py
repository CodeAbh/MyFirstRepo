# def greet():
#     print("good evining")
#     print("aks")
#     return 10

# x=greet()
# greet()
# print(x)

# def add():
#     x=10
#     y=20
#     return x+y
# x=add()
# print(add()+10)
# print(add())
# print(add()-50)
# print(x)


def calc():
    x=10
    y=20
    z=x+y
    p=x-y
    q=x*y
    r=y/x
    return z,p,q,r

# a=calc()
# print(a)
# print(type(a))
a,b,c,d=calc()
print(a,b,c,d)
print(type(a))
