import re

re_email=re.compile(r'([\w\.]+)@(\w+).com')

S=str(input('Please input your email:'))

#S='danxie@cisco.com'

 
if re_email.match(S):
	print("{} is valid.\n{} is valid employee.".format(S,re_email.match(S).group(1)))
else:
	print("{} is not a valid email address".format(S))

input("END")
