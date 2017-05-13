#!/usr/bin/env python3

from functools import wraps

def decorator_func(original_func):
#    @wraps(original_func)
    def wrapper_func(*args,**kwargs):
        print ('call function %s()' % original_func.__name__)
        return original_func(*args,**kwargs)
    return wrapper_func


def decorator_func2(original_func):
#    @wraps(original_func)
    def wrapper_func(*args,**kwargs):
        print ('call function %s() again' % original_func.__name__)
        return original_func(*args,**kwargs)
    return wrapper_func
	
	
#@decorator_func
#@decorator_func equals to 
#display=decorator_func(display)
def display():
    print('display function ran')

#display()
#@decorator_func2
#@decorator_func
def display_info(name,age):
    print('name is %s and age is %s' % (name,age))

display_info=decorator_func(display_info)
display_info('Dan',31)
#print(display_info.__name__)
	
#display_info('Dan',31)