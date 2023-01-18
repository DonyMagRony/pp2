#Insert the missing part of the code below to output "Hello World".
print("hello world")
#This example misses indentations to be correct.
#Insert the missing indentation to make the code correct:
if 5 > 2:
    print("Five is greater than two!")

#Comments in Python are written with a special character, which one?
    #This is a comment
#Use a multiline string to make the a multiline comment:
"""
This is a comment
written in 
more that just one line
"""
 

#Create a variable named carname and assign the value Volvo to it.
carname="Volvo"
#Create a variable named x and assign the value 50 to it.
x=50
#Display the sum of 5 + 10, using two variables: x and y.
x=5
y=10
print(x+y)
#Create a variable called z, assign x + y to it, and display the result.
x=5
y=10
z=x+y
print(z)
#Remove the illegal characters in the variable name:
myfirst_name = "John" #2my-first_name = "John"
#Insert the correct syntax to assign the same value to all three variables in one code line.
x=y=z="orange"
#Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
  global x
  x = "fantastic"


#The following code example would print the data type of x, what data type would that be?(7)
x = 5
print(type(x))  
int
x = "Hello World"
print(type(x))
str
x = 20.5
print(type(x))
float
x = ["apple", "banana", "cherry"]
print(type(x))
list
x = ("apple", "banana", "cherry")
print(type(x))
tuple
x = {"name" : "John", "age" : 36}
print(type(x))
dict
x = True
print(type(x))
bool


#Insert the correct syntax to convert x into a floating point number
x = 5
x = float(x)
#Insert the correct syntax to convert x into a integer
x = 5.5
x = int(x)
#Insert the correct syntax to convert x into a complex number.
x = 5
x = complex(x)


#Use the len method to print the length of the string.
x = "Hello World"
print(len(x))
#Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
#Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
#Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
#Replace the character H with a J
txt = "Hello World"
txt = txt.replace("H", "J")
#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am{}"
print(txt.format(age))


#The statement below would print a Boolean value, which one?
print(10 > 9)
True
#The statement below would print a Boolean value, which one?
print(10 == 9)
False
#The statement below would print a Boolean value, which one?
print(10 < 9)
False
#The statement below would print a Boolean value, which one?
print(bool("abc"))
True
#The statement below would print a Boolean value, which one?
print(bool(0))
False


#Multiply 10 with 5, and print the result.
print(10*5)
#Divide 10 by 2, and print the result.
print(10/2)
#Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
#Use the correct comparison operator to check if 5 is not equal to 10.
if 5!=10:
    print("5 and 10 is not equal")
#Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")


#Print "Hello World" if a is greater than b.
a = 50
b = 10
if a >b:
    print("Hello World")
#Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a!=b:
    print("Hello World")
#Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a==b:
    print("Yes")
else:
    print("NO")
#rint "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")
#Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
    print("Hello")
#Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
    print("Hello")    
#This example misses indentations to be correct.Insert the missing indentation to make the code correct:
if 5 > 2:
    print("Five is greater than two!")
#Use the correct short hand syntax to put the following statement on one line:
if 5 > 2: print("Five is greater than two!")
#print("Yes") if 5 > 2 else print("No")