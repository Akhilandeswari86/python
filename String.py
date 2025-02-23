# Explain about String.

#--------------------------------------------------


#A string is a sequence of characters. Python treats anything inside quotes as a string. This includes letters, numbers, and symbols. Python has no character data type so single character is a string of length 1.
#Strings can be created using either single (‘) or double (“) or triple (""") quotes.
#Strings are indexed starting from 0 and -1 from end.
#String is immutable.



# example1
str="Aditya";
print(str[4]);
print(str)

#example2
x="this is her name";
print(x);

#example3
y="""Hello World"""
print(y)

#example4
num='Arjun'
print(num)

#example5
j="nani is a hero"
print(j)

#example6
nani="He is a employee"
print(nani)

#example7
bindu='her age is 25'
print(bindu)

#example8
nandu="""hello kitty"""
print(nandu)
#example9
a="bujji"
print(a)

#example10
gopi="hyd"
print(gopi)


# explain index and slice


# Index:
# Index is Classified into two types:
# 1. Positive Index
# 2. Negitive Index
# using Index we can access  only one Element.
# Slice :
# using slice we can access group of Elements in a list.
# Slice follows n-1 notation
# because Index starts with 0. 


# example1
str="Aditya";
print(str[4]);
print(str[0:4])
print(str)

#example2
x="this is her name";
print(x[-5])
print(x[-1:-8])

print(x);

#example3
y="""Hello World"""
print(y[8])
print(y[-6:-10])
print(y)

#example4
num='Arjun'
print(num[3])
print(num[1:3])
print(num)

#example5
j="nani is a hero"
print(j[9])
print(j[6:10])
print(j)

#example6
nani="He is a employee"
print(nani[9])
print(nani[1:10])
print(nani)

#example7
bindu='her age is 25'
print(bindu[-6])
print(bindu[6:10])
print(bindu)

#example8
nandu="""hello kitty"""
print(nandu[-2])
print(nandu[-8:10])
print(nandu)

#example9
a="bujji"
print(a[-3])
print(a[-1:-5])
print(a)

#example10
gopi="hyd"
print(gopi[-3])
print(gopi[-2])
print(gopi)



#concatenation : String concatenation means add strings together. Use the + character to add a variable to another variable.
#example1
a="hello"
b="world"
con=a+" "+b
print(con)

#example2
gopi="beauty"
gopi1="eyes"
con=gopi+" "+gopi1
print(con)

#example3
num="manju"
num1='22'
con=num+num1
print(con)

#example4
jubbi="teks"
jubbi1="academy"
con=jubbi+" "+jubbi1
print(con)

#example5
b="har"
c='shitha'
con=b+c
print(con)



# Repating :  In repeat() we give the data and give the number, how many times the data will be repeated. If we will not specify the number, it will repeat infinite times.

#example1
a="how are you" " "
print(a*3)

#example2
num="Good Morning"  " "
print(num*10)


#example3
ganesh="hello hyd" " "
print(ganesh*5)

#example4
chanu='this is paragarph' " "
print(chanu*20)

#example5
b="good job" " "
print(b*10)

#example6
c="nice" " "
print(c*20)





# Explain all Methods

# lower() : Converts all uppercase characters in a string into lowercase.
a="Teks Academy "
print(a.lower())
# upper() : Converts all lowercase characters in a string into uppercase.
a="Teks Academy"
print(a.upper())
# len()   : returns the length of a string.
name="City of Density"
print(len(name))
# strip() : The method removes spaces at the start and end of the string.
ganesh=" city of density "
print(len(ganesh))
srtp=ganesh.strip()
print(ganesh.strip())
print(len(srtp))

# split() : method splits a string into a list of strings after breaking the given string by the specified separator.
num="I am from Rajamandry"
print(num.split())

# join () : method to combine a list of strings into a single string with each string separated by a space.

num=['I', 'am', 'from', 'Rajamandry']
print(' '.join(num))


# define tuple

# Python Tuple is a collection of objects separated by commas.
# Tuples are used to store multiple items in a single variable.
# It is immutabule.


#example1
b=(1,4,6,7,"exam")
print(b)


# example2
joy=(20,"this","hello",2+8j)
print(joy)
print(joy[3])
print(joy.count(20))
print(len(joy))


# example3
kitty=("kittu",1,5,3,6,3,2,1,"kittu")
print(kitty)
print(kitty[5])
print(kitty[-7:-1])
print(len(kitty))

# example4

smitha=(2.8,8.44,5+3j,"hiiiiii")
print(smitha)
print(smitha[-3])
print(smitha[1:4])
print(len(smitha))

# example5

nani=(1,4,3,2,7,8,6,4,9,0)
print(nani)
print(nani[5])
print(nani[-6:-3])
print(len(nani))