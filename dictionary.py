# define dictionary:

# A Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.
# a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.
# Python dictionary are Ordered.
# Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly.
# Keys must be immutable: This means keys can be strings, numbers, or tuples but not lists.
# Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
# We can access a value from a dictionary by using the key. 
#example1
dic={"name":"akhila","age":50,"location":"rjy"}
print(dic)
print(type(dic))

#methods : 
#keys() : Returns a view object that displays a list of all the keys in the dictionary.
a={"id":1,"name":"ammu","age":23,"num":10}
print(a.keys())
#values() : Returns a view object containing all dictionary values.
a={"id":1,"name":"ammu","age":23,"num":10}
print(a.values())
#items() : Return the list with all dictionary keys with values.
a={"id":1,"name":"ammu","age":23,"num":10}
print(a.items())
#pop() : Returns and removes the element with the given key.
a={"id":1,"name":"ammu","age":23,"num":10}
print(a.pop("num"))
#get() : Returns the value for the given key.
a={"id":1,"name":"ammu","age":23,"num":10}
print(a.get("gender"))
#clear(): Removes all items from the dictionary.
a={"id":1,"name":"ammu","age":23,"num":10}
print(a.clear())
#update(): Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs. With this method, you can include new data or merge it with existing dictionary entries.

a={"id":1,"name":"ammu","age":23,"num":10}
b={"gender":"female"}

a.update(b)

print(a)




#examples
dect={"id":1,"name":"hema","weight":60,}
print(dect)
print(dect.keys())
print(dect.values())
print(dect.items())
print(dect.popitem())
print(dect.get("weight"))
print(dect.clear())
print(dect)
dect={"id":1,"name":"hema","weight":60,}
c={"vill":"ram"}
print(dect.update(c))
print(dect)



#example2
loc={"hyd":"charminar","kerala":"murgan","warangal":"1000 pillar"}
print(loc)
print(loc.keys())
print(loc.values())
print(loc.items())
print(loc.popitem())
print(loc.get("ts"))
print(loc.clear())
print(loc)

#example
num={"id":1,"loc":"ap","roll":"smart"}
print(num)
print(num.keys())
print(num.values())
print(num.items())
print(num.pop("id"))
print(num.get("name"))
print(num.clear())
print(num)
num={"id":1,"loc":"ap","roll":"smart"}
num1={"name":"joy"}
num.update(num1)
print(num)


#example
j={"leela":"uday","seetha":"bujji","jogi":"lakshmi"}

print(j)
print(j.keys())
print(j.values())
print(j.items())
print(j.popitem())
print(j.get("seetha"))
print(j.clear())
j={"leela":"uday","seetha":"bujji","jogi":"lakshmi"}
b={"gowri":"ravi"}
j.update(b)
print(j)
     