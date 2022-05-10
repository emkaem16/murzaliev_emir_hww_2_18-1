class Company:


    def __init__(self, company_bank, company_name,):
        self.company_bank = company_bank
        self.company_name = company_name


    def Person_info(self):
        print(f"{self.company_bank}\n{self.company_name}")




class Person(Company):

    def __init__(self, company_bank, company_name, first_name, last_name, salary):
     super().__init__(company_bank, company_name,)
     self.first_name = first_name
     self.last_name = last_name
     self.salary = salary

    def get_salary(self):
        if self.company_bank < self.salary:
            print("У компании не достаточно средств!")
        else:
            print(self.company_bank - self.salary)

    def person_info(self):
        print(f"""
        Company: {self.company_name}
        Company Bank: {self.company_bank}
        Person : {self.first_name} {self.last_name}
        Salary: {self.salary} 
            """)




work = Person(90000, "apple", "Emir", "Murzaliev", 1500)
work.person_info()
work.get_salary()