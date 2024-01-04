#variables that created outside of the function are known as global variables
x= "awesome"
def myfunc():
    print("python"+x)
    
myfunc()

#use the global keyword if you want to change a global variable inside a function

m="aw"
def my():
    global m 
    m= "fun"
my()
print("python is"+ m )