'''#default
def student(name="Ramya"):
    print("Hello",name)
student()
student("Divya")
#keyword
def  student(name,id):
    print("Name:",name)
    print("Id:",id)
student(name="Divya",id=24099401)
#positional
def student(name,age):
    print("Name:",name)
    print("Age:",age)
student("divya",18)'''
#1
def full_name(first_name,last_name):
    print(f"Hello,{first_name}{last_name}")
full_name("Divyadharshini","Sivanpandian")
#2
def power(base,exponent=2):
    result=base**exponent
    print(f"the power of {base} is {result}")
power(9)
#3
def student_profile(name,course,year):
    print("Name:",name)
    print("Course:",course)
    print("Year:",year)
student_profile(name="Divya",course="BE",year="2nd yr")
#4
def marks (*marks):
    result=sum(marks)
    total=len(marks)
    avg=result/total
    print("Total marks=",result)
    print("Average=",avg)
marks(10,20,30,40,50)
#5
def student_info(**info):
    for key,value in info.items():
        print(f" {key}:{value}")
student_info(name="divya",age=18,year=2)
#6
square=lambda x:x*x
print("the square is:",square(9))
#7
add=lambda a,b:a+b
print("Sum=",add(5,7))
