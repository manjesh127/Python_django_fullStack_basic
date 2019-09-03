
# class Circle():

#     pi=3.14

#     def __init__(self,radius=1):
#         self.radius = radius
#     def area(self):
#         return self.radius*self.radius*Circle.pi
# my = Circle(3)
# my.radius=100            #another way to define radius
# print(my.area())


#----------------    or fixed radius ------

class Circle():

    pi=3.14

    def __init__(self,radius=1):
        self.radius = radius
    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self,new_rad):
        self.radius = new_rad


my = Circle(3)
my.set_radius(9)
print(my.area())