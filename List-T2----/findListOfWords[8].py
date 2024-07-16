'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to find the list of words that are longer than n from a
given list of words.
'''


def words_longer_than_n(words_list, n):
    
    longer_words = [word for word in words_list if len(word) > n]
    return longer_words


words_list = ["hello", "world", "python", "programming", "code"]
n = 5
result = words_longer_than_n(words_list, n)
print(result)  # Output: ['python', 'programming']
