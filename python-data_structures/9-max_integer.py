#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (0, None)
    biggest_number = my_list[0]
    for number in my_list:
        if number > biggest_number:
            biggest_number = number
    return biggest_number
