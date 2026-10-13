file=open("Sample.txt","w")
user_inp=input("Enter your input: ")
file.write(user_inp)
file.close()


print("--------------------")
file=open("Sample.txt","r")
a=file.read()
print("Output of a the above file: ")
for i in a:
    print(i,end="")
file.close()