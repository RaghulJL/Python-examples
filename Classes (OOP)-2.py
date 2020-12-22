class Computer:
    def __init__(self):
        self.name="Name: J.L.Raghul"
        self.age="Age: 20"

    def update(self):
        self.name="Name: Rahul J.L"
        self.age="Age: 21"
    
c1=Computer()
print(c1.name)
print(c1.age)

c1.update()

print("The updated entry is:")
print(c1.name)
print(c1.age)