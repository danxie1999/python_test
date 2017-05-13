#!/usr/bin/env python3

class std:
    pass_grade=60
    no_of_std=0
    def __init__(self,first,last,grade):
        self.first=first
        self.last=last
        self.grade=grade
        std.no_of_std+=1
    @property
    def fullname(self):
        return "%s %s" % (self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
    @property
    def email(self):
        return "%s.%s@company.com" % (self.first,self.last)
    def grade_pass(self):
        if not self.grade >= self.pass_grade:
            return self.fullname + " does not pass"
        else:
            return self.fullname + " does pass"
    @classmethod
    def set_pass_grade(cls,amount):
        std.pass_grade=amount
    @classmethod
    def from_string(cls,string):
        first,last,grade=string.split('-')
        return cls(first,last,grade)
    @staticmethod
    def is_schoolday (day):
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        else:
            return True	
        
        
print(std.no_of_std)
std_1=std('Dan','Xie',90)
std_2=std('Tony','Chen',91)
print(std.no_of_std)

print('%s %s' %(std_1.first,std_1.last))

std_1.first="Bruse"

print(std_1.fullname)

print(std_1.email)

std_1.fullname="Pitt Zhang"
print(std_1.fullname)

print (std_1.grade_pass())
#std.pass_grade=95
std.set_pass_grade(96)
print (std_1.grade_pass())

std_str_1="Pit-D-87"
std_str_2="Neil-P-85"
std_str_3="James-L-60"

new_std_1=std.from_string(std_str_1)

print(new_std_1.grade)

from datetime import date

day=date(2017,3,7)

print(std.is_schoolday(day))



