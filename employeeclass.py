#!/usr/bin/env python3

class Employee:
	mount_of_raise=1.04
	no_of_emps=0

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email="{}.{}@company.com".format(self.first,self.last)
		Employee.no_of_emps+=1

	def fullname(self):
		return "{} {}".format(self.first,self.last)

	def apply_pay(self):
		self.pay=int(self.pay * self.mount_of_raise)

	@classmethod
	def set_raise_mount(cls,amount):
		cls.mount_of_raise=amount

	@classmethod
	def from_string(cls,emp_string):
		first,last,pay=emp_string.split('-')
		return Employee(first,last,pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() ==6:
			return False
		return True

print(Employee.no_of_emps)

emp_1=Employee('Dan','Xie',50000)
emp_2=Employee('Tony','Chen',60000)

##print(emp_1.email)
#print(emp_1.fullname())

#print(emp_1.__dict__)

#print(Employee.__dict__)

#Employee.set_raise_mount(1.05)

#print(emp_1.pay)
#emp_1.apply_pay()
#print(emp_1.pay)
#print(Employee.no_of_emps)

#emp_str_1='Pit-Hat-70000'

#new_emp_1=Employee.from_string(emp_str_1)

#print(new_emp_1.fullname())

import datetime

TD=datetime.date(2017,3,20)

print(Employee.is_workday(TD))