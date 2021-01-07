import time
n=int(input("Enter a number: "))
for i in range(n):
    if n<2:
        time.sleep(0.5)
        print("Enter a valid no.")
        break
    elif n==2:
        time.sleep(0.5)
        print("Prime no.")
        break
    else:
        if (n%2==0):
            time.sleep(0.5)
            print("Not a Prime no.")
            break
        else:
            time.sleep(0.5)
            print("Prime no.")
            break
time.sleep(0.5)
print("BYE! BYE!")