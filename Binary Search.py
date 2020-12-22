pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
lst=list([])
k=int(input("Enter the length of list:"))
for i in range(k):
    x=int(input("Enter next value:"))
    lst.append(x)
print(lst)
n=int(input("Enter the no. to search:"))
if search(lst,n):
    print("Found at",[pos])
else:
    print("Not found")