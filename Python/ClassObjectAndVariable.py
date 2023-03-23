class employee:
    salary = 120
    def myFunc(self):
        print(f"Salary is {self.salary}")
Arihant = employee()
Aayushmaan = employee()
Arihant.salary = 500
Aayushmaan.salary = 499
Arihant.myFunc()
employee.myFunc(Arihant)
Aayushmaan.myFunc()