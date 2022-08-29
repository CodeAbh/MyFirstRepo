l=[x for x in range(1,11)]
print(l)
l1=[2**x for x in range(6)]
print(l1)
l2=[3**x+x for x in range(5)]
print(l2)
# # l3=['a','x' ,'y','z','i']
# # l4=[]
# # vowel=['a','e','i','o','u']
# # for ele in l3:
# #     if ele in vowel:
# #         l4.append(ele) 
# print(l4)
l3=['a','x','y','z','i']
vowel=['a','e','i','o','u']
l4=[ele for ele in l3 if ele in vowel]
print(l4)

