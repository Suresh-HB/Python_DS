'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python program for histogram
'''

def create_histogram(data):
    frequency = {}

    for number in data:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

            """ frequency is the dictionary 
            that holds integer as a keys and valus"""
    for key in sorted(frequency.keys()): #here sorted()-is the built function python that return list in sorted form
        print(f"{key}: {'*' * frequency[key]}")


if __name__ == "__main__":
    numbers = [1, 30, 30, 5, 6, 7, 8, 8, 8, 10, 10]
    create_histogram(numbers)
