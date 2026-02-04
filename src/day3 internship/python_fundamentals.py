name="umar"
print(name)
print(type(name))

age=20.0
print(age)
print(type(age))

num1=10
num2=20
sum=num1+num2
sum2=num1*num2
print(sum2)

sum3=num1/num2
print(sum3)

#task 1

user_name=input("enter your name:")
user_age=(input("enter your age:"))
user_age=int(user_age)
user_age=user_age+4
print(f"hey {user_name}, you will be {user_age} years old in 2030")

#practic 1

user_name=input("enter your name")
user_address=input("enter yuor city name")
uder_dateofbirth=int(input("enter your date of birth"))
user_age=int(input("enter youe age"))
user_age+=10
print(f"hey{user_name}your city is{user_address}you will be {user_age}year old will be in 2036")

#task2
totalbill=float(input("enter your amount"))
number_of_people=int(input("enter numberofpeople"))
share_per_person=totalbill/number_of_people
print(f"{totalbill}each person pay {share_per_person}")

#task3
item_name="laptop"
quantity=2
price=499.9
in_stock=True
print(item_name,quantity,price,in_stock)
totalcost=quantity*price
print(totalcost)

day3 internship

student_list=["heer",24,8.86]
print(student_list)

car_detail=["bmv",4000000,5]
print(car_detail) # car,price,year

student_list=[10,20,30,40,50,60]
print(student_list) 
#add data in list
student_list=[10,20,30,40,50,60,70]
student_list.append("100")
student_list.pop(2)
print(student_list)

#task1
inventory=["apple","banana","carrots","dates"]
inventory.append('egg')
inventory.remove('banana')
inventory.sort()
print(inventory)

#task2
tempreature=[22,24,25,28,30,29,27,26,24,22]
print(tempreature[0:-1])
tempreature[3:6]
tempreature[-3:]
print("printing the\"afternoon peak(4th,5th,6th iteam)",tempreature[3:6])
print("printing the\"last 3 hour",tempreature[-3])

#task3
screen_res=(1920,1080)
print("current Resolution:1920x1080")
#screen_res[0]=1280
print("Tuples cannot be modify")
