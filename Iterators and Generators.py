#ITERATORS IN PYTHON
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            vls=self.num
            self.num+=1
            return vls
        else:
            raise StopIteration
values=topten()
print("First Output")
for i in values:
    print(i)

#GENERATORS IN PYTHON
def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
val=topten()
print("\n")
print("Second Output")
for i in val:
    print(i)

#SQUARE USING GENERATORS IN PYTHON
def toptwenty():
    n=1
    while n<=20:
        sq=n*n
        yield sq
        n+=1
vals=toptwenty()
print("\n")
print("Third Output")
for i in vals:
    print(i)
