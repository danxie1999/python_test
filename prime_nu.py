#!/usr/bin/env

def prime_nu (n):
    print('{}='.format(n),end='')
    if not isinstance(n,int) or n <=0:
	    print('{} is not a number'.format(n))
    elif n==1:
        print('{}'.format(n))
        

def cycle (m):
    for x in range(2,m+1):
        if m % x ==0:
            m=int(m/x)
            if m==1:
                print(x)
                exit(0)
            else:
                print('{}*'.format(x),end='')
                return cycle (m)
            
                
					

nu=int(input('Please input a number:\n'))
					
prime_nu(nu)

if nu >1:
    cycle(nu)