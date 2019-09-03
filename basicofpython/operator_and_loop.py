# if 1<2:
#     print("First condition in block")

#     if 20<3:
#         print("Second condion in block")

#----------------------- else if 

# if 1>2:
#     print("if execute")
# else:
#     print("else execute")    


#------------------------ multiple if else 
# if 1==1:
#     if 1>2:
#         print("hello")
#     elif 3==3:
#         print("else if exec")
#     else:
#         print("last")        

#--------------------------for loop
# seq = [1,2,3,4,5,6]
# for item in seq :                 #item name (any) must be stor the loop value 
#     #--write code here- 
#     # print(item)
#     print("hello")

#------for loop in dictionary
# d = {"man":1,"rahu":2,"shik":3}

# for dickey in d :
#     print(dickey)
#     print(d[dickey])

#----------------list of truples
# mypair = [(1,2),(3,4),(5,6)]        #list of three truples

# for item in mypair:         #print all truples
#     print(item)

# for truple1,truple2 in mypair:            #unpacking all truple
#     print(truple1)
#     print(truple2)

#-----------------------------while loop
# i=1
# while i<5:
#     print("i is:{}".format(i))
#     i=i+1

#-----------------------------------------------control flow and range function 
# for item in range(10):
#     print(item)

#--------list comprihension
x = [1,2,3,4]

squr = []
multi=[]
# for a in x :
#     squr.append(a**2)
#     multi.append(a*2)
# print(squr) 
# print(multi)   
#----or
squr = [num**2 for num in x]              #another method
print(squr) 