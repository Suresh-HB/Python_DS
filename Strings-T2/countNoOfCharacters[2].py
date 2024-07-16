'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to count number of character present in string.

'''


def main():

    test_str = "GeeksforGeeks"
    all_freq = {}

    for i in test_str:

        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    print("Count of all characters in GeeksforGeeks is :\n "+ str(all_freq))


if __name__ == '__main__':
    main()