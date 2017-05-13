#!/usr/bin/env python3

#list=[1,2,3,4,5]

#for i in list:
 #   print (i)
#    if i == 3:
#        break
#else:
#    print ('this is a no break')


def find_index (to_research,target):
    for index,value in enumerate(to_research):
        if value == target:
            return index        
            break
    else:
        return -1

list=['Tim','Dan','Jack','Tom']

print(find_index(list,'Xiao'))