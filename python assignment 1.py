# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print(" Python got successfully installed on my PC")

#problem 2
for x in range(2000,3201):
   if x%7 ==0 and x%5!=0:
        print (x , end=", " )
       
 # printing the sequence as a list
 
result=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        result.append(x)
        
print("Result = " + str(result))


# problem 3       
first_name = input(" enter your first name : ")
last_name= input("enter your last name: ")
revfirst_name= first_name[::-1]
revlast_name=last_name[::-1]
print (revfirst_name + " " + revlast_name)


#problem 4
diameter=12
r= diameter/2
v1= 4/3 * 3.14 * r**3
#v2= 4/3 * 3.14 * r*r*r
print (v1)
#print (v2)










        





