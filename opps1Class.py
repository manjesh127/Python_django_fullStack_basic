class Sample():
    pass

x= Sample()
# print(type(x))  
  
#--------------------------------------
print("""  2nd example   """)
class Dog():
    pass

mydog = Dog()
# print(type(mydog))    

#--------------------------------------
print("""  3rd example   """)
class Hello():
    def __init__(self,breed):
        self.breed = breed

x = Hello(breed="lab")
# print(type(x))
# print(x.breed)

y = Hello(breed="hii2")               #breed is the instance of the class object
# print(y.breed)

#---------------------------
#--------------------------------------
print("""  4rd example   """)
class Man():
    #class object attributes
    species = "manual"
    def __init__(self,sin,jon):
        self.sin = sin
        self.jon=jon

a= Man("sinArg","jonArg")
print(a.sin)
print(a.jon)
print(a.species)