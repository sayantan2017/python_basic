#python allow you to assign values to multiple variables in one line
x,y,z ="orange","Banana","Mango"
print(x)
print(y)
print(z)

#one value in multiple variables

x=y=z = "Mango"
print(x)
print(y)
print(z)

#unpack a collection
#if you have a collection of values in a list , tuple etc, pythonn allow you to extract the values into variables . this is called unpacking

fruits=["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)