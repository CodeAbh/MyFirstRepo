# def csd(n):
#     if n>2:
#         csd(n-1)
#         print("hello")
#     print(n+5)
# csd(6)

# def csd(n,x):
#     if n>1:
#         x=x+2
#         return csd(n-1,5)+x+n
#     else:
#         return 15
# result=csd(3,7)
# print(result)


# def csd(n):
#     if n>1:
#         return csd(n-1)+n
#     else:
#         return 5
# result=csd(4)
# print(result)





def csd(n):
    if n>2:
      return csd(n-1)+n
    else:
         return 4

result=csd(6)
print(result)
