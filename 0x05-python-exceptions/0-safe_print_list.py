#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []

    count = 0
    if x < 0:
        return count

    if x > len(my_list):
        x = len(my_list)

    for i in range(x):
        print(my_list[i], end="")
        count += 1

    print()
    return count
