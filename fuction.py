def pure_func(list):
    new_list=[]
    for i in list:
        new_list.append(i**2)
    return new_list
original_list=[1,2,3,4]
modified_list=pure_func(original_list)
print("original list:",original_list)
print("modified list:",modified_list)
    
    
