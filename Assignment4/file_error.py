file_name=input("Enter your file name with extension: ")
try:
    
    file=open(f"{file_name}","r")
    a=file.readlines()
    print("Output of a the above file: ")
    counter=0
    for i in a:
        counter+=1
        print(f"Line {counter}: {a[counter-1]}")
    file.close()
except:
    print(f"{file_name} not Found")