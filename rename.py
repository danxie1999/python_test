#!/usr/bin/env python3

import os

os.chdir('C:/python_test/test/rename')

os.path.split('C:/python_test/test/rename')

for f in os.listdir():
    f_name,f_ext =os.path.splitext(f)
    f_title,f_course,f_num=f_name.split('-')
    f_title=f_title.strip()
    f_course=f_course.strip()
    f_num=f_num.strip()[1:].zfill(2)
    f_rename="%s-%s-%s%s"%(f_num,f_course,f_title,f_ext)
    os.rename(f,f_rename)