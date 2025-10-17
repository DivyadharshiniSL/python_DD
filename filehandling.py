'''f=open("Hi.txt","r")
content=f.read()
print(content)
f.close()'''
'''#using with
with open("Hi.txt","r") as f:
 content=f.read()
 print(content)
#readline()
 with open("Hi.txt","r") as f:
  line1=f.readline()
  line2=f.readline()
  print(line1,line2)
#readlines()
  with open("Hi.txt","r") as f:
     line=f.readlines()
     print(line)'''

#write()
with open("Hi.txt","w") as f:
  f.write("Bonjour")
  f.write("this is French")

  #writelines()
lines=["line1\n","line2\n"]
with open("example.txt","w") as p:
    p.writelines(lines)
#append
with open("example.txt","a") as p:
    p.write("\nline is appended")