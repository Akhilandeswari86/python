# Example about Lists


# a list is a built-in dynamic sized array.
# We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is possible.
# List in Python are Mutable. Hence, we can modify, replace or delete the items.
# List can representing "[ ]"".
# Every Element separate "[ , ]"".



# List Examples:



# Example 1
a=[1,3,6,5,9];
print(type(a));


# Example 
b=[4,"akhila",4.5,4+9j];
print(b);


# Example 3
ab=["jio","idea","airtel"];
print(type(ab));


# Example 4
num=[3,5,9,0,2,3,5];
print(num);

# Example 5
vyshu=[1,9,"teks"];
print(vyshu);

# Example 6
c=[2.0,5.1,66,94.6];
print(type(c));

# Example 7
nani=[1,"nani",24,"hyd"];
print(nani);






# Explain about Index and Slice


# Index:
# Index is Classified into two types:
# 1. Positive Index
# 2. Negitive Index
# using Index we can access  only one Element.
# Slice :
# using slice we can access group of Elements in a list.
# Slice follows n-1 notation
# because Index starts with 0.

# example 1
teks=[1,3,7,9,3,0,2];
print(teks[4]);
print(teks[2:7]);
# example 2
a=[1,2,3,4,5,6,7,8,9];
print(a[3:7]);
print(a[4]);

# Example 3
raju=[1,"sasi",20,'rjy','java'];
print(raju[4]);
print(raju[1:4]);


# example 4
basha=[3,"raju",46,"km",200.2,1,0,5555]
print(basha[4]);
print(basha[5:6]);

# example 5
j=[1,4,5,8,9,3,22,55,8,3333,00.3,9,2];
print(j[9]);
print(j[1:8]);


# example 6
y=[1,2,3,4,5,6,7,8,9,10,2,44,5];
print(y[8]);
print(y[-4:-9]);


# example 7
b=[9,3,4,5,7,8];
print(b[-1:-4]);


# example 8
a=[3,7,5,9,0];
print(a[-3]);


# example 9
i=[3,'teks',22,"java",'hyd',30000];
print(i[3]);
print(i[-2:6]);

# example 10
ashi=['fn','joe',22,5,"i",'m','n'];
print(ashi[1]);
print(ashi[2:6]);



# Explain list types

# 1.append():
# Adds an element at the end of the list.
# example:
a=[1,2,3,4,5,6]
a.append(2)
print(a)

# 2. extend():
# Adds multiple elements to the end of the list.
# example :
a=[1,3,5,4,6,2,7]
b=[0,3,2,5]
a.extend(b)
print(a)

# 3.pop():
# Removes the element at a specific index or the last element if no index is specified.
# example :
a=[2,5,6,5,3]
a.pop()
print(a)

# 4.len():
# the length of a paticular list.
a=[1,2,3,4,5,6,7,8,9,2]
print(len(a))


# 5.count():
# how many times a element is present.
a=[1,3,4,2,6,1,4,6,8,5,7]
print(a.count(1))
