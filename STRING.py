#!/usr/bin/env python3

i=input('Please input something:\n')

letter=0
space=0
number=0

for j in i:
    if j.isalpha():
        letter+=1
    elif j.isdigit():
        number+=1
    elif j.isspace():
        space+=1

print('letter numberis %s, number is %s, space number is %s' % (letter,number,space))		