'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Concatinating the given dictionaries in to a new dictionary
'''

def concateToDictionary(dic1,dic2,dic3):
    """
    Description: Function to store the user inputs dictionaries into dictionary
    Parameter: 
    dic1,dic2,dic3, : taking three individual dictionaries
    Return:
    result_dict : returning the concatinated new dictionary
    """


    result_dict = {**dic1, **dic2, **dic3}
    print(result_dict)

    # l1=len(dic1)
    # l2=len(dic2)
    # l3=len(dic3)
     # how to optimize this code for finding length    
    # length=l1+l2+l3
    # print(type(length))
    
    # res=my_dictionary={}
    # for i in dic1:
    #     my_dictionary[i]=dic1.get(i)
    #     # print(i, dic1.get(i)) for printing value and key
    
    # for i in dic2:
    #     my_dictionary[i]=dic1.get(i)

    # for i in dic3:
    #     my_dictionary[i]=dic1.get(i)

    # return my_dictionary


def main():

    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}

    concateToDictionary(dic1,dic2,dic3)
    # res=concateToDictionary(dic1,dic2,dic3)
    # print(res)

if __name__ == '__main__':
    main()











