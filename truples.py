#------------------------booleans
True
False

#-----------------------truples
t = (1,2,3)
# print(t[0])
t2=("man",1,2,4,True,"mannj")
# print(t2)

# t2[1]="manj"      #truples are not supported assignment   list support assignment 
# print(t2)


#------------------------sets
#--- sets is unorder collection of unique elelment-----------
x = set()

x.add(1)
x.add(2)
x.add(3)
# x.add(0.1)
x.add(4)
x.add(4)                                 #if add 4 multiple time only 1 time 4 is added because set is unique elelment add
x.add(4)
print(x)

convert = set([1,1,1,2,2,2,3,3,3,4,5,5,6,6,6,7,7,7,8])

print(convert)