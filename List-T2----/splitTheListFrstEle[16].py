'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to split a list based on first character of word.
'''

def split_list_by_first_character(words):
    grouped_lists = {}
    for word in words:
        first_char = word[0]
        if first_char in grouped_lists:
            grouped_lists[first_char].append(word)
        else:
            grouped_lists[first_char] = [word]
    return grouped_lists


def main():
    words = ["apple", "banana", "pear", "avocado", "orange", "grape", "peach"]
    grouped_lists = split_list_by_first_character(words)
    for key in sorted(grouped_lists.keys()):
        print(f"Words starting with '{key}': {grouped_lists[key]}")


if __name__ == '__main__':
    main()
