#Programmer: Jordan Gibbs
#Program Variables & Methods
#Date: 1.11.2024
 
quote = "All is fair in love and war!" #Variable is quote and the value of the variable is the string "All is fair in love and war!" 
#Methods are functions that are avaukuble for a given object

print(quote)
print(quote.upper()) #The .upper makes the quote all uppercase also known as a method
print(quote.lower()) #The .lower makes the quote all lowercase also known as a method
print(quote.title()) #The .title puts it in Titlecase also known as a method
print(len(quote)) #The len lists the amount of charactets in our quote variable
 
name = "Jordan Gibbs" #String
age = 15 #int is the number left of the decimal if their is one
gpa = 4.0 #float is the number right of a decimal 
 
print(age)
print(int(gpa)) #int casts the float into an integer

#Note that anytime you print a casted int it will not round up so instead of 3.7 rounding up to 4 it will instead be 3

print("\nMy name is " + name + ", and I am " + str(age) + " with a GPA of " + str(gpa) + ".") #The + concatenates the variables while s"tr" casts the variables "age" and "gpa" which are integers into a string without adding space 

print("\nMy name is",name,"and I am",str(age),"with a GPA of",str(gpa) + ".") #The , concatenates the variables while the "str" casts the variables "age" and "gpa" which are integers into a string and also adds a space.

#Note that it reads program like a book top to bottom and left to right.

print("")

age += 1 #adds one to the variable age which now has a value of 26
print(age)

print("")

age += 10 #adds ten to the variable age
print(age)

print("")
 
birthday = 1 #adds the birthday variable that has a value of 1 to the age variable that now has a value of 37. You can only add if if the values are int.
age += birthday
print(age)
