class Employee:
    e_name="Rahul"
    e_id=101
    e_sal=50000
    def Disply(self):
        print("Employee Name:-",self.e_name)
        print("Employee Id:-",self.e_id)
        print("Employee Salary:-",self.e_sal)
    def calculate_anual_salary(self):
        Anual=self.e_sal*12
        print("The Anual Salary Of Employee is:--",Anual,"RS")
obj=Employee()
obj.Disply()
obj.calculate_anual_salary()