#!/usr/bin/env python3

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def case (s):
    return s[:1].upper()+s[1:].lower()

print(list(map(case,['adam', 'LISA', 'barT'])),end='')