def f1(n):
    print(n)
    if n>0:
        f1(n-1)
    print(n+3)
f1(3)