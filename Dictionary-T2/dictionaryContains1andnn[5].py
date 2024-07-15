'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
'''


def do_dictionary(n):
    """
    Description : Function to stores the key, and value is key*key and print the dictionary 
    Parameter: Function taking the n as a user input parameter
    Return:
        dict1 : returning the concatinated new dictionary
    """


    dic={}
    for i in range(n+1):
        if i == 0:
            continue
        else:
            value=i*i
            dic[i]=value
    return dic
    

def main():
    n=int(input("Enter the value of N\n"))
    res=do_dictionary(n)
    print(res)


if __name__ =='__main__':
    main()



