#!/usr/bin/env python3
p=4



try:
    a=1
    b=0
    1/0
except ZeroDivisionError:
    print("zerodivision error")
    raise
finally:
    print("print this code no matter what")
	

