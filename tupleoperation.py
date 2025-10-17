#packing
tup_1="hello",31,28.9
print(tup_1)
#unpacking
a,b,c=tup_1
print(a)
print(b)
print(c)

#operations
tup_2=(2,30,60,90,60)
print(len(tup_2))
print(max(tup_2))
print(min(tup_2))
print(tup_2.count(60))
print(sum(tup_2))
print(tup_2.index(60))


tup_3=90,30,"welcome",40.1,75
a,*b,c=tup_3
print(a)
print(*b)
print(c)
