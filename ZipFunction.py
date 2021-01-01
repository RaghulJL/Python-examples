names = ("Rahul JL", "Rajath", "Abhishek")
comps = ("TCS", "Cognizant", "Wipro")
zipped = zip(names, comps)
for (a,b) in zipped:
    print(a, "is working in", b)