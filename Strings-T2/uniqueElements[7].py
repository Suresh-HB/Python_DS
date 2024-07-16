'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form.

'''


def uniqueSort(inputWords):

    """
    Description: Function to iterate the input and stores the elements into 
                set ensures the uniquenes, then sort the set using sort method.
    Parameter:
       inputWords: Function taking (inputWords) as a parameter in to the function.
    Return: 
    """


    wordsList = [word for word in inputWords.split(',')]
    uniqueWords = set(wordsList)

    sorted_words = sorted(uniqueWords)

    result = ", ".join(sorted_words)
    
    print("Sorted unique words:", result)


def main():

    inputWords = input("Enter a comma separated sequence of words: ")
    uniqueSort(inputWords)


if __name__== '__main__':
    main()