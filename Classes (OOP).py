class Computer:
    def __init__(self, CPU, RAM, Storage):
        self.CPU=CPU
        self.RAM=RAM
        self.Storage=Storage

    def config1(self):
        print("Configuration 1 is:",self.CPU,self.RAM,self.Storage)

    def config2(self):
        print("Configuration 2 is:",self.CPU,self.RAM,self.Storage)

com1=Computer("Core i5 9th Gen,","8GB RAM,","1TB HDD")
com2=Computer("Ryzen 5-3500U,","8GB RAM,","512GB SSD")

Computer.config1(com1)
Computer.config2(com2)