class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        salary10 = self.salary*1.1
        print(int(salary10))

arthur = Employee('Arthur', 3600)
arthur.show()