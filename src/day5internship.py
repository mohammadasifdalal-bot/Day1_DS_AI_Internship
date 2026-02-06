#defining functions


def greet():
    print("welcome to comed kares")
   
greet()

def display_line():
    print("--------")
    
display_line()

def add(a,b):
    print(a+b)
    
result=add(2, 5)#passing parameters
print(result)#empty

x=10#global

def show_value():
    x=5#local
    print(x)
show_value()

print(x)

#chnaging global
x=5
def show():
    global x
    x=20
show()
print(x)

x=0
def addi():
   global x
   x+=1
addi()
print(x)


import math
import random

print(math.sqrt(5))
print(random.randint(10, 100))

