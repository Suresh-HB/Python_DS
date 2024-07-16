'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Program to Sort the value in raising order
'''


def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

def main():
    sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_list = sort_by_last_element(sample_list)
    print("Sorted List:", sorted_list)

if __name__ == "__main__":
    main()


