#Programmer: Jordan Gibbs
#Program: Functions
#Date: 1.19.2024

age = 3 #global variable

def nl():
	print('\n')


def who_am_i(): #This is a function without parameters 
	name = "Jordan" #Called a local variable because its local to the function
	age = 16 
	print("My name is",name,"and I am",age,"years old.")
	
who_am_i() #To call function you just have to name it and put parentheses to set the parameters

nl()

age += 20

print(age)

nl() 

def addOneHundred(num): #num is a Parameter. Note that you can call the Parameter anything you want
	print(num + 100)

addOneHundred(50) #50 is the Arguement which inserts itself into the parameter

nl()

addOneHundred(0)

nl()

def add(x,y): #Their are two parameters
	print(x + y)
	
add(8,4) # 8 & 4 are the operands 





