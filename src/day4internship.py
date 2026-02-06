student={"name":"asif","age":21,"course":"engineering"}
print(student["name"])
student["age"]=21
student["city"]="bangalore"
student["village"]="harsoor"
print(student)

directory={"mark":"hundred","age":12,"sumester":"eight"}
print(directory["mark"])
directory["name"]="mutaheer"
directory["home"]="my home"
print(directory)

#task1
contacts={"mutaheer":8888,"saqeeb":9999,"umar":7777}
print(contacts)
contacts["asif"]=5555 #adding
contacts["mutaheer"]=0000 #updating

#safe access
print(contacts.get("saqeeb","saqeeb ka kata so hai"))

for a, b in contacts.items():
    print(f"contacts: {a} | phone {b}")


#tasks2
raw_logs=["ID01","ID02","ID03","ID01","ID08","ID02","ID05"]
unique_users=set(raw_logs)

print("ID05" in unique_users)    


duplicates = len(raw_logs)-len(unique_users)
print("total duplicates removed are ",duplicates)

#practic

raw_logs=["id01","id02","id03","id01","id04","id03"]# list
unique_users=set(raw_logs)#set
print("id04" in  unique_users)#id04 check karna hai
duplicate=len(raw_logs)-len(unique_users)#in dono me duplicate check karna hai
print("total duplicates removed are ",duplicates)

#task3
friend_a={"python","cooking","Hiking","movies"}
friend_b={"hiking","gaming","photography","python"}

share_interests=friend_a&friend_b
all_interests=friend_a|friend_b
unique_to_a=friend_a-friend_b

print(share_interests)
print(all_interests)
print(unique_to_a)



 