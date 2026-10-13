val=int(input("Enter the number of Student Name & Marks you want to enter: "))
dic={}
for i in range(1,val+1):
    a=input(f"{i} Student name: ")
    b=input(f"{i} the Marks: ")
    dic[a]=b
print(dic)


user_inp=input("Enter Student Name: ")
if user_inp in dic.keys():
    print(f"Marks of the {user_inp}: {dic[user_inp]}")
else:
    print(f"{user_inp} Not Found in Dictionary")