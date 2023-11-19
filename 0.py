class Employee ():
    def __init__(self, number, name, sales, bonus_hrs, bose_salary):
        self.nunber=number
        self.name=name
        self.sales=sales
        self.bonus_hrs=bonus_hrs
        self.bose_salary=bose_salary

    def info(self) :
        print("les caraketer de employe","name",self.name,"bose_salary",self.bose_salary,"sales",self.sales)


emp1 = Employee(1,"yahya",40000,50000,555)
emp1.info()



