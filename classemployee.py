#!/usr/bin/env python3

class Employee:
    raise_amount=1.04
    no_of_emps=0
    def __init__(self,first,last,gender,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.gender=gender
#        self.fullname='%s %s' % (self.first,self.last)
        Employee.no_of_emps+=1
    @property
    def email(self):
        return '%s.%s@compant.com' % (self.first,self.last)

    @property
    def fullname(self):
        return '%s %s' % (self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print("%s is deleted" % self.fullname)
        self.first=None
        self.last=None

	
    def apply_raise(self):
	    self.pay=int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount (cls,amount):
        cls.raise_amount= amount
    @classmethod
    def from_string(cls,string):
        first,last,gender,pay = string.split('-')
        return cls(first,last,gender,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    def __repr__(self):
        return "Employee('%s','%s','%s',%s)" % (self.first,self.last,self.gender,self.pay)
    def __str__(self):
        return "%s %s" % (self.first,self.last)
    def __add__(self,other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
		
class Developer(Employee):
    raise_amount=1.10
    def __init__(self,first,last,gender,pay,prog_lang):
        super().__init__(first,last,gender,pay)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,gender,pay,employees=None):
        super().__init__(first,last,gender,pay)
        if employees == None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp (self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp (self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps (self):
        for emps in self.employees:
            print("-->",emps.fullname())
        
		
#print(Employee.no_of_emps)
#emp_1= Employee('Dan','Xie','male',10000)
#emp_2= Employee('Tony','Chen','male',12000)		
dev_1= Developer('Dan','Xie','male',10000,'Python')
dev_2= Developer('Tony','Chen','male',12000,'Shell')		

#print(dev_1)

#print(dev_1 + dev_2)

#print(len('test'))
#print('test'.__len__())

#print(dev_1.__len__())

#print(int.__add__(1,2))
#print(str.__add__('a','b'))

#print (dev_1.pay) 
#dev_1.apply_raise()
#print (dev_1.pay)
#print (dev_1.prog_lang)
mrg_1=Manager('Shawn','He','male',20000,[dev_1])
mrg_2=Manager('Shawn','Liu','male',20000)
#print(help(Developer))

#print(isinstance(mrg_1,Manager))
#print(issubclass(Manager,Employee))
#mrg_2.add_emp(dev_2)
mrg_1.remove_emp(dev_1)
#mrg_1.print_emps()
mrg_2.print_emps()

dev_1.first='Pit'

print(dev_1.first)
print(dev_1.email)
print(dev_1.fullname)
dev_1.fullname="Zhang San"
print(dev_1.fullname)

del dev_1.fullname
print(dev_1.fullname)


#print(Employee.no_of_emps)

#print(emp_1.email)
#print(emp_1.fullname())
#print (emp_1.pay)

#Employee.set_raise_amount(1.05)

#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
#print(Employee.raise_amount)
#print(Employee.__dict__)
#print(emp_1.__dict__)
#print (emp_1.pay)

emp_str_1 = 'John-T-male-30000'
emp_str_2 = 'Teddy-D-male-40000'
emp_str_3 = 'Pit-R-male-50000'


emp_str_1= Employee.from_string(emp_str_1)

#print(emp_str_1.first,emp_str_1.pay)


import datetime
my_date= datetime.date(2017,3,5)

#print (Employee.is_workday(my_date))


#self: an instance 
#init: an instance method (constructor) receive first argument as an instance,
#first: another argument (attribute)
#self.first: instance varible
# raise_amount: a class varible
# set_raise_amount: an class method
# a class method can work as a alternative constructor 
# from_string: alternative constructor
# is_workday: a staticmethod (have a logical connection with the class)
# @property define a method and access it as a attribute