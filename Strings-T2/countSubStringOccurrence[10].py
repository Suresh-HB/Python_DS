'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to count occurrences of a substring in a string.

'''


def count_substring_occurrences(main_string, substring):
    
    """
    Description : Function to count how many substrings are present in the the given string.
    
    Parameter :
       main_string : as a parameter for counting substrings from the main_string.
       substring : this for identifiy the substring from the given string and count.
    
    Return: 
        main_string.count(substring) :  returning the substring count.
    """

    return main_string.count(substring)


def main():

    main_string = input("Enter the sentence\n")
    print("You entered sentence")
    
    print(main_string)
    
    substring = input("Enter which word occurrence you want to count from your sentence : ")
    
    count = count_substring_occurrences(main_string, substring)
    
    print(f"The substring '{substring}' occurs {count} times in the main string.")


if __name__ == '__main__':
    main()