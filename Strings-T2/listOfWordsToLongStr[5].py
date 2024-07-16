'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python function that takes a list of words and returns the length of the longest
one.

'''


def wordsString(s):

    if not s: 
        return 0
    
    return max(len(word) for word in s)


def longest_word(words):

    """
    Description : Function to find out the longest string in list.
    Parameter :
       words : Function taking (words) as a parameter in to the function.
    Return: 
        max : returning the max length of the word.
    """


    if not words:  
        return ""
    return max(words, key=len)


def main():

    slist=['java', 'python','sql','working']
    res=longest_word(slist)
    print(res)


if __name__ == '__main__':
    main()


