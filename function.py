# def my_fun(param="default"):
#     print("my first function {}".format(param))

# my_fun()

#-------------------function 2
# def hello():
#     #  print("hi")
#     return "hi"

# man = hello()
# print(man)

#----------------------function 3

# def add_number(a,b):
#     if(type(a)==type(b)==type(10)):                         
#         return a+b
#     else:
#         return "sorry please enter integer value"

# res = add_number(2,3)           #add as a number argument
# # res = add_number("2","3")         #add as a string argument
# print(res)
# print(type(res)) 

# ------------------------lambda expressions

#---filter
# mylist = [1,2,3,4,5,6,7]

# def even_bool(num):
#     return num%2==0

# evens = filter(even_bool,mylist)                          #filter function is pass function argument and value to filter
# print(list(evens))                                        #list method are use to get resp of filter function

# evens = filter(lambda num:num%2 == 0,mylist)           #lamda give same output 
# print(list(evens))

#-------------------string function
# string = "hii i am! #manjesh"

# splvalue = string.split('#')[0]
# print(splvalue)

#-----------------------------
print('x' in [1,2,3,4])
print('x' in [1,2,3,'x'])