#Linear search algorithm
pos=-1
def search(list,n):
    i=0
    for i in range(len(list)):
        if list[i]==n:
            globals() ['pos']=i
            return True
            break
    return False
#Getting values
ls=list([])
s=int(input("Enter the length of the list:"))
for i in range(s):
    x=int(input("Enter next value:"))
    ls.append(x)
print(ls)
#Searching
n=int(input("Enter the value to search:"))
if search(ls,n):
    print("Found at",[pos])
else:
    print("Sorry! Not found")