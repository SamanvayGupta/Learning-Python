a=int(input("Enter the number: "))

def fact(a):
    var=1
    for i in range(1,a+1):
        var=var*i
    return var
print(f"Factorial of {a} is: {fact(a)}")

def factor(a):
    if a == 1 or a == 0:
        return 1
    return a * factor(a-1)

print(f"Factorial of {a} is: {factor(a)}")
