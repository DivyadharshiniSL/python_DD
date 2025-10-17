student_names=[]
student_marks=[]
num_students=int(input("how many students?"))
for i in range(num_students):
    name=input(f"Enter student name{i+1}:")
    mark=int(input(f"Enter marks of{name}:"))
    student_names.append(name)
    student_marks.append(mark)
print("\n----All students records----")
for i in range(len(student_names)):
    print(f"{student_names[i]} - {student_marks[i]} marks")
highest=max(student_marks)
lowest=min(student_marks)
average=sum(student_marks)/len(student_marks)
print("\n---Statistics---")
print("Highest mark:",highest)
print("Lowest marks:",lowest)
print("Average:",average)
print("\n---Passed students---")
for i in range(len(student_names)):
    if student_marks[i]>=40:
        print(f"{student_names[i]} - {student_marks[i]}")
print("\n---Failed students---")
for i in range(len(student_names)):
    if student_marks[i<40:]:
        print(f"{student_names[i]} - {student_marks[i]}")
