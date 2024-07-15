'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : 
'''


def doCheck(color_list_1,color_list_2):
    lsc1=list(color_list_1)
    lsc2=list(color_list_2)
    x=[]
    for i in lsc1:
            if i in lsc2: 
               continue
            else:
                x.append(i)
    print(set(x))           
   

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

doCheck(color_list_1,color_list_2)
