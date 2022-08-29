# IS-A relation

# class P:
#     x=100
#     def __init__(self):
#         print("constructor")
#     def m1(self):
#         print("instant variable")
    
#     @classmethod
#     def m2(cls):
#         print("class method")

#     @staticmethod
#     def m3():
#         print("static method")

# class c(P):
#     pass
# c=c()
# c.m1()
# c.m2()
# c.m3()


# class P:
#     x=100
#     def __init__(self):
#         self.p=10
#     def m1(self):
#         self.q=20

# class C(P):
#     y=200

# c=C()
# print(c.x,c.y,c.p,)
# c.m1()
# print(c.x,c.y,c.p,c.q)


# class P:
#     x=100

# class C(P):
#     def m1(self):
#         super().__init__()
#         print("instant variable")
        

# c=C()
# print(c.x)




# Type of inheritance
# class A:
#     def m1(self):
#         print('A-m1')
# class B(A):
#     def m2(self):
#         print('B-m2')

# class C(B):
#     def m3(self):
#         print("C-m3")

# class D(C):
#     def m4(self):
#         print('D-m4')

# d=D()
# d.m1()
# d.m2()
# d.m3()
# d.m4


# class A:
#     def m1(self):
#         print('A-m1')
# class B:
#     def m2(self):
#         print('B-m2')

# class C(A,B):
#     def m3(self):
#         print("C-m3")

# c=C()
# c.m1()
# c.m2()
# c.m3() 


# HAS-A relation
# class Engine:
#     def start(self):
#         print('engine-start')

# class Car:
#     def use_engine(self):
#         e=Engine()
#         e.start()

# c=Car()
# c.use_engine()

# class Engine:
#     @staticmethod

#     def start():
#         print('engine-start')

# class Car:
#     def use_engine(self):
#         e=Engine()
#         e.start()

# c=Car()
# c.use_engine()


# class Engine:
#     def __init__(self):
#         self.a=10
#     def start(self):
#         print('engin-start')

# class Car:
#     def __init__(self,modle,en):
#         self.model= modle
#         self.en=en
#     def use_engine(self):
#         print(self.model)
#         self.en.start()
#         print(self.en.a)

# e=Engine()
# c=Car('xyz',e)
# c.use_engine()
# print(e.a)
# print(c.en.a)

# class Car:
#     def __init__(self,model,color):
#         self.model=model
#         self.color=color
#     def getInfo(self):
#         print(self.model)
#         print(self.color)

# class Employee:
#     def __init__(self,eid,esalry,car):
#         self.eid=eid
#         self.esalry=esalry
#         self.car=car
#     def display(self):
#         print(self.eid)
#         print(self.esalry)
#         self.car.getInfo()


# c=Car('venu','black')
# e=Employee(1,2000,c)
# # e.display()
# e.car.getInfo()

# composition & aggregation 

# class Student:
#     Cname='cpt'
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

# print(Student.Cname)
# print(rollno)


#super()

# class Parent:
#     x=100
#     def __init__(self):
#         self.a=10

# class Child(Parent):
#     y=200
#     def __init__(self):
#         super().__init__()
#         self.b=20

# c=Child()
# print(c.x,c.y,c.a,c.b)



# class Parent:
#     x=100
#     def __init__(self,a,x):
#         self.a=a
#         Parent.x=x

# class Child(Parent):
#     y=200
#     def __init__(self,a,x,b):
#         super().__init__(a,x)
#         self.b=b

# print(Parent.x)
# c=Child(50,300,150)
# print(c.x,c.y,c.a,c.b)
# print(Parent.x)

# def Csd():
#     print("csd")
# def Csd1():
#     print('csd1')
#     return 10

# x=Csd()
# y=Csd1()
# z=Csd
# z1=Csd1
# Csd=Csd1
# z()
# z1()
# Csd()
# Csd1()
# # x()
# # y()



# def Csd():
#     print("csd")

# x=Csd()
# z=Csd()
# # print(x)
# print(Csd is z)
# print(Csd is x)
# del Csd
# print(id(x))
# print(id(z))
# # x()
# z()
# Csd()


# def Csd():
#     print("csd")

# z=Csd
# print(id(Csd))
# print(id(z))
# print(Csd is z)

