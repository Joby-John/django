# python doesnt support different number of variable , same function name(overloading) as in other languages

#method overriding

class Employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def printDetails(self):
        print(f"ID: {self.id}, Name: {self.name}")

class SalesEmployee(Employee):
    def __init__(self, id, name, amount):
        super().__init__(id, name)
        self.salesAmount = amount
    
    def printDetails(self):
        super().printDetails()
        print(f"Amount: {self.salesAmount}")

employees = [Employee(101, 'Sandeep'), SalesEmployee(102, 'Rahul', 5000)]

for emp in employees:
    emp.printDetails()


#operator overloading(exists in cpp also but not in java)
# magic methods or dunder methods:  __add__, __lt__, __le__, __eq__, __ne__, __gt__, __ge__, __sub__, __mul__, etc 
class Product:
    def __init__(self, product, price):
        self.product = product
        self.price = price
    def __add__(self, other):
        return({f"{self.product}, {other.product}":self.price + other.price})

p1 = Product("keyboard", 500) 
p2 = Product("Mouse", 300)
print(p1+p2) 
                