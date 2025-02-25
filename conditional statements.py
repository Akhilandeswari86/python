# Conditional Statements:

# 1.If Statement
number=10
if number>0:
 print("it is positive") 

 #-------------------------------------------------------------------------   
 

# 2.else Statement
number=int(input("enter your number:"))
if number>0 :
 print("It is Positive")
else:
 print("It is Negative")

 #--------------------------------------------------------------------


# 3.else if statement
number=int(input("Enter Your Number:"))
if number>0:
 print("positive")
else :
     if number<0:
       print("Negative")

     else:
       print("It is Zero")

#------------------------------------------------------------------------------

# example:
age=int(input("Enter Your Age:"))
if age>18:
  print("You are Eligible")
else:
  print("you aren't Eligible")


#example :
age=int(input("Enter Your Age:"))
if age<21:
  print("Go to College")
else :
      if age>21 and age<60:
        print("Go to Work")
      else:
        
        print("Go to Retire")

#example :
# python code to find given number is even or odd ?
num=int(input("Enter the Number:"))
if num%2==0:
  print("Given Number is Even")
else:
  print("Given Number is Odd")



  #example :
  # python code to find given char is vowel or not vowel?
  Char=input("Enter Your Char:")
  vowel=['a','e','i','o','u']
  if Char in vowel:
    print("It is a Vowel",Char)
  else:
    print("It is not Vowel",Char)

  if Char.lower() in vowel:
    print("vowel",Char)
  else:
    print("Not Vowel",Char)

#-------------------------------------------------------------------------------------------------


# write a python program to find maximum of three numbers. Find which is the maximum.
num1 = 10
num2 = 30
num3 = 15
if (num1>=num2) and (num1>=num3):
  print("the maximum number is num1")
elif (num2>=num1) and (num2>=num3):
  print("the maximum number is num2")
elif (num3>=num1) and (num3>=num2):

  print("the maximum number is num3")
else:
  print("the maximum num is:")





# write a python program to design grading system.
std=int(input("Enter the Marks:"))
Marks = 100
if Marks>=90:
  print("grade:A",std)
elif Marks>=80:
  print("grade:B",std)
elif Marks>=70:
  print("grade:C",std)
elif Marks>=60:
  print("grade:D",std)
elif Marks>=50:
  print("garde:E",std)
else:
  print("Your are Fail")



# write a python program swap of two numbers without using third variable.
a=3
b=4
c=a+b
b=c-b
a=c-a
print(a)
print(b)


# write a python program swap of two numbers with using third variable.

x=30
y=39
z=x+y
y=z-y
x=z-x
print(x)
print(y)

# write a python program to reverse a string.
name="Akhila" [::-1]
print(name)

# write a python program to check given year is leap year or not.
year=int(input("enter a year:"))
if year%4==0:
  print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")


# write a python program to find minimum number among 4.
num1=5
num2=26
num3=41
num4=3
if (num1<=num2) and (num1<=num3) and (num<=num4):
  print("the minimum number is num1")
elif (num2<=num1) and (num2<=num3) and (num2<=num4):
  print("the minimum number is num2")
elif (num3<=num1) and (num3<=num2) and (num3<=num4):
  print("the minimum number is num3")
elif (num4<=num1) and (num4<=num2) and (num4<=num3):
  print("the minimum number is num4")
else:
  print("the minimum number is:")







