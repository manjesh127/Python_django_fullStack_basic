# print('hello)                
#---1---output SyntaxError:----

# mylisthere = [1,2,3,4,5]
# print(mylist) 
#----2----NameError:---


#-------------create file----- simple without error handling
# f = open('simple.txt','r')                                         # ---w write the file if using in place of r then give error
# f.write("Text write to simple txt")
# print("hii")




#------------------------example---solution for handle-------
# try:
#     f = open('simple.txt','w')                                         # ---w write the file if using in place of r then give error
#     f.write("Text write to simple txt")

# except IOError:                                                         #--note if dont know exception simple use except:
#     print("ERROR:could not find file or read")

# else:
#     print("success")
#     f.close()    
    

#----------------------2nd way -----------------------
try:
    f = open('simple.txt','r')                                        
    f.write("Text write to simple txt")
     #in try block dont have syntax error because it affect both except and finnaly block and error 

except :                                                         
    print("ERROR:could not find file or read")

finally:
    print("I always work no matter what")
    