#inheritance 

#-------------1st create base class --------
class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")    

    def eat(self):
        print("eating")    

# mya = Animal()
# mya.whoAmI()
# mya.eat()

#-----2nd--------------now inheriat ---------
class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self) 
        print("dog Created")


# mydog = Dog()
# mydog.eat()
# mydog.whoAmI()

#---------------3r --------- special method-----
class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        # return "hello self method"
        return "Title :{}, Author :{}, Pages :{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is distroy")    



b= Book("python","manjesh",200)
# print(b)
# print(len(b))
del b
