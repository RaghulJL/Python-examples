def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

print("Select Operation:")
print("1.Add", end=" ")
print("2.Subtract", end=" ")
print("3.Multiply", end=" ")
print("4.Divide")

while True:
    choice=input("Enter your choice: ")
    if choice in ('1','2','3','4'):
        num1=float(input("Enter 1st no.: "))
        num2=float(input("Enter 2nd no.: "))
        if choice=='1':
            print(add(num1,num2))
        elif choice=='2':
            print(subtract(num1,num2))
        elif choice=='3':
            print(multiply(num1,num2))
        elif choice=='4':
            print(divide(num1,num2))
        break
    else:
        print("Invalid input")