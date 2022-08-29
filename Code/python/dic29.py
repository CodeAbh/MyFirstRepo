# d={'abc':80,'pqr':30,'lmn':30}
# print(type(d))
# print(d)
# d['xyz']=90
# print(d)
# d['pqr']=70
# print(d)

# d={}
# print(type(d))
# print(d)
# d['xyz']=70
# print(d)
# d['pqr']=80
# print(d)

# d={'abc':80,'pqr':30,'lmn':30}
# print(d.get('abc'))
# print(d.get('xyz'))
# print(d.get('xyz',10))


# st='abac'
# d={}
# for ch in st:
#     d[ch]=d.get(ch,0)+1

# print(d)


d={'abc':80,'pqr':50,'lmn':60}
print(d)
print(d.pop('abc'))
print(d)
print(d.popitem())