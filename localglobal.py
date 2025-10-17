x= 10
def show():
    x=80
    print(x)
show()
print(x)

count=5
def sum():
    global count
    count+=1
    print(count)
sum()