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

