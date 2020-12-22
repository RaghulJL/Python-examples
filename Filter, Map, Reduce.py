nums=list([])
m=int(input("Enter the length of list: "))
for i in range(m):
    x=int(input("Enter the next value: "))
    nums.append(x)
print(nums)

#Filtering
odds=list(filter(lambda n : n%2!=0, nums))
print("The filtered \'odd\' list is: ", odds)
evens=list(filter(lambda n : n%2==0, nums))
print("The filtered \'even\' list is: ", evens)

#Mapping
from functools import reduce
doubles1=list(map(lambda n : n*2, odds))
print("The doubled odd list is: ", doubles1)
doubles2=list(map(lambda n : n*2, evens))
print("The doubled even list is: ", doubles2)

#Reducing
sum1=reduce(lambda a,b : a+b, doubles1)
print("The sum of \'doubles1\' is:", sum1)
sum2=reduce(lambda a,b : a+b, doubles2)
print("The sum of \'doubles2\' is:", sum2)