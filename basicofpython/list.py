# mylist = [1,2,3,4]
# mylist = ["manjesh",1,2,3,2.3,True,[1,2,3]]
# print(mylist[:3])
# mylist[1] = "manjesh"        #assignment
# mylist.append("singh")          #append
# mylist.extend([1,2,3,'manjesh'])
# mylist.pop(2)   #remove 2 position data in list
# print(mylist)

# ---------------------------
# a =[1,2,3,[1,"e","a","m"]]
# print(a[3][1])

#----------------------------
matrix = [[1,2,3],[4,5,6],["p","q","r"]]
# print(matrix[0][0])

#list comprehension
firstcol = [row[0] for row in matrix]    #first element in each list
print(firstcol)