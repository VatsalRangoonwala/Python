# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, location):
        self.name = name
        self.salary = salary
        self.address = location

vatsal = programmer("vatsal", 120000, "surat")
print(vatsal.name, vatsal.company, vatsal.salary, vatsal.address) 

yash = programmer("yash", 20000, "surat")
print(yash.name, yash.company, yash.salary, yash.address) 