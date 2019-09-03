x = 25

def myfun():
    x =50
    return x

# print(x)    
# print(myfun())

myfun()
# print(x)

#-----------------2 enclosing fun local ------
name = "this is a global name"

def greet():
    name = "manjesh"

    def hello():
        print("hello func "+name)
         
    hello()

greet()  

# print(name)

#------------------3  built in python ---------------
x =50

def firstfun():
    global x                   #global key make the variable globaly when after the calling function
    x = 1000


print("x before calling function:",x)    
firstfun()
print("x after call function :",x)

#--------------or same function another way---------
y =50

def test():
    # global x                   #global key make the variable globaly when after the calling function
    y= 1000
    return y

print("x before calling function:",y)    
y = test()
print("x after call function :",y)