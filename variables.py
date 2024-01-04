#variables do not need to declared with any particular type and can even change type after they have been set.

x=5 # X is of type int
y="Sayantan" # y is of type string
print(x)
print(y)

x=4 # x is type of int
x="dd" # now x is type of string
print(x)

# if you want to specify the data type of a variable , this can be done with casting
x= str(3)
y= int(88)
z=float(80)
print(x)
print(y)
print(z)

# we can get the datatypes of variables with the type() function

x=5
y='John'
print(type(x))
print(type(y))

#string variables can declared either by using single or double quotes

x="john"
x= 'jhon'

#variable name is case sensitive
a=4
A="Saaa"
# A will not overwrite a