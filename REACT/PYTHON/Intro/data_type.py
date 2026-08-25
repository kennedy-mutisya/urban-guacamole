#example variables
x=10            #Integer
y=3.14          #Float
z="hello"       #string
a=True          #Boolean<True, False>
b=[1,2,3,4]     #list <Array> Mutable <By value>
c={1,2,3}       #Set
d=(1,2,3)       #Tuple <list> immutable
e={"key": "value"}
#Dictionary <objects: js>
#for dictionary use bracket notation

#determining the types
#'y is ${}'
print("x is ",x, "its type", type(x)) #output: <class 'int'>
print(f"y is {y} its type {type(y)}") #output : <class 'float'>
print(f"y is {z} its type {type(z)}") #output : <class 'str'>
print(f"y is {a} its type {type(a)}") #output : <class 'bool'>
print(f"y is {b} its type {type(b)}") #output : <class 'list'>
print(f"y is {c} its type {type(c)}") #output : <class 'set'>
print(f"y is {d} its type {type(d)}") #output : <class 'tuple'>
print(f"y is {e} its type {type(e)}") #output : <class 'dict'>
