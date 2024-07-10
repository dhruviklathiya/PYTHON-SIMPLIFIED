_list = [1,2,3,4,[1,2,3],[1,2],[1]]
total_list = 0
for i in range(0,len(_list)):
    if type(_list[i]) == list:
        total_list+=1
print("Total number of list in single list is: ",total_list)