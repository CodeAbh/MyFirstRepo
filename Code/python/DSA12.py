# n=6
# for i in range(n,0,-1):
#     num=65
#     for j in range(1,i+1):
#         print(chr(num),end=" ")
#         num=num+1
#     print()
# n=6
# for i in range(1,n+1):
#     num=65
#     for j in range(1,i+1):
#         print(chr(num),end=" ")
#         num=num+1
#     print()

n=6
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()
n=6
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()
