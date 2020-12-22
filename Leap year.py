num=int(input("Enter the year:"))
if (num%4==0):
    if (num%100==0):
        if (num%400==0):
            print("Leap Year")
            print("BYE BYE!")
        else:
            print("Not a Leap Year")
            print("Get Lost!")
    else:
        print("Leap Year")
        print("BYE BYE!")
else:
    print("Not a Leap Year")
    print("Get Lost!")
print("HAVE A NICE DAY")
