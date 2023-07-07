""" This a test file"""

from abc import ABCMeta , abstractmethod , abstractstaticmethod

class IDepartment(metaclass= ABCMeta):
    @abstractmethod
    def __init__(self) :
        """ implement in child"""

    @abstractstaticmethod
    def print_department():
        """ implement in thechild class"""

class Accounting(IDepartment):
        def __init__(self,employees):
            self.employees = employees
        def print_department(self):
            print(f"accounting department : {self.employees}")

class Secops(IDepartment):
        def __init__(self,employees):
            self.employees = employees
        def print_department(self):
            print(f"secops department : {self.employees}")
    

class ParentDep(IDepartment):

        def __init__(self,employees):
            self.employees = employees
            self.base_employees = employees
            self.sub_depts= []
        def add(self,dept):
            self.sub_depts.append(dept)
            self.employees += dept.employees

        def print_department(self):
            print("Parent dep")
            print(f"Parent dep Base employyes: {self.base_employees}")
            for dept in self.sub_depts:
                dept.print_department()
            print(f"total number of employyes : {self.employees}")

dept1= Accounting(200)
dept2= Secops(150)
dept3= Secops(5) 
parent_dep = ParentDep(50)
parent_dep.add(dept1)
parent_dep.add(dept2)

parent_dep.print_department()


