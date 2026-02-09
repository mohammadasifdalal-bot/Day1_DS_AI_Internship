#reading file
file=open("new.txt",'r')
content=file.read()
print(content)
file.close()


#writing file
file=open("new.txt",'w')
file.write("welcome to my channel")
file.close()
