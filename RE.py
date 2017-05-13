import re,time


L=['','10.146.90.1 UP','10.146.90.101 UP','10.146.90.102 UP','10.146.90.106 UP','10.146.90.11 UP']

print(sorted(L,key=lambda nu: int(nu.split()[0].split('.')[-1])))
