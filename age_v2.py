#!/usr/bin/env python3

age=int(input("Please let me know how old are you:"))
name=str(input("Please inout your name:"))
city=str(input("Please let me know which city are you in:"))

if age>18:
    print("You are an adult named",name,"lives in", city)
else:
    print("You are a teenager named",name,"lives in",city)

