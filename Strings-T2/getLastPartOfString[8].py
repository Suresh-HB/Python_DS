'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to get the last part of a string before a specified character.

'''


def get_last_part_before_character(main_string, character):
        
    """
    Description : Function to returns the string before specified character.
    
    Parameter :
        main_string : is the original string 
        character : After this character whatever string is present that will excluded.
    
    Return: 
        character.join(parts[:-1]) : returning the string before present in character
    """
    
    index = main_string.find(character)
    
    if index != -1:
        return main_string[:index]
    else:
        return "character not found"
    


def main():

    main_string = "https://www.w3resource.com/python-exercises"

    character = "*"
    result = get_last_part_before_character(main_string, character)
    print(f"The last part of the string before '{character}' is: '{result}'")


if __name__ == '__main__':
    main()

