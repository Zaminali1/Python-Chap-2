# Strings:
# Strings are used to store text data in python.
# A string is a sequence of characters.
# Declaring a string

str_1="HEllo"  # we can use single quotes or double quotes for declaring strings.
Str_2='world'

# if we put \n in a string it will print the next string in the next line.
str_3=("This is me.\n Hello!")
print(str_3)

# String Concatenation
# We can concatenate two strings using + operator.
str_4 = str_1 + Str_2
print(str_4) # Output: Helloworld

# length of a string
# We can find the length of a string using len() function.
str_5 = "ABCD"
str_6 = "EFGH"
Str_7 = len(str_5 + str_6)
print(Str_7) # Output: 8

# indexing in strings
# We can access the characters of a string using index.
str_8 = "Hello"
str_9= str_8[1]
print(str_9) # Output: e

# STRING FUNCTION
hik=("i am programmer")
print(hik.replace("m","n"))

# 1: WAP to input user's first name and print its length
user=input("Enter Your First Name :")
print("Length of your name is ", len(user))

# 2: WAP to find occurrence of h in string:
user2=("helloh hethrow ")
print(user2.count("h"))

# CONDITIONAL STATEMENTS
light=("Gre")
if (light=="Green"):
     print("Go")
else:
     print("Wait")

Age=25
status="Adult" if Age>=23 else "Minor"
print(status)

# Assign grades to student based on marks...
marks = int(input("Enter You'r Marks: "))
if marks >= 95 and marks < 100:
    grade= "A++"
elif marks >= 90 and marks < 95:
    grade = "A+"
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 40 and marks < 70:
    grade = "C"
else:
    grade = "F" 

print("You Got ", grade ,"Grade" )

Age= 40
if (Age >= 18):
    if (Age>=80):
        print("You can not drive")
    else:
        print("You can drive")

# Nesting
student=3
if(student >=5):
    if (student<=2):
     print("They can not go")
    else:
     print("They can go")
else:
      print("Come here")

# Practice:
# Write a program to check if number entered by user is odd or even
num= int(input("Enter Number : "))
rem=num%2
if(rem == 0):
    result="Even"
else:
    result="Odd"
print("Number is ",result)

# 2. WAP to check if a number is multiple of 7 or not.
Num2=int(input("Enter Number To Check It is Multiple of Seven Or Not: "))
rem2=Num2%7
if(rem2==0):
  print("The Number You Entered is Multiple of 7")
else:
    print("The Number You Entered is not Multiple of 7")
