#reading file
file=open("new.txt",'r')
content=file.read()
print(content)
file.close()


#writing file
file=open("new.txt",'w')
file.write("welcome to my channel")
file.close()

#topic2

with open("sample.txt","r") as file:
    content=file.read()
    print(content)
    
    #topic3
import csv
with open("data.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        
  #topic4
try:
    with open("new.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found error, please check the filename")   

#task1

contents=input("Please enter the user name and daily goal:" )

#using appending
with open ("journal.txt",'a') as file:
    file.write(contents)
with open ("journal.txt",'a') as file:
    file.write(contents)
with open ("journal.txt",'a') as file:
    file.write(contents) 

#using reading    
with open ("journal.txt","r") as file:
    contents=file.read()
    print(contents)
    
 #use input function

#w is for writting
   
with open ("journal.txt",'w') as file:
    file.write(contents)
with open ("journal.txt",'w') as file:
    file.write(contents)
with open ("journal.txt",'w') as file:
    file.write(contents)
 
#r for reading    
with open ("journal.txt","r") as file:
    contents=file.read()
    print(contents)
    
  
#task2    
import csv

with open("student.csv","r") as file:
    reader=csv.DictReader(file)
    
    print("student who has passed:")
    for row in reader:
        if row ["Status"]=="Pass":
            print(row["Name"])    
    
#task3

filename = input("Enter the filename ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile contents:\n")
        print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")