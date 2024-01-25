#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    elif idx == 0:
        my_list = my_list[1:]
        return my_list
    else:
        list_1 = my_list[0:idx]
        list_2 = my_list[(idx + 1):]
        my_list = list_1 + list_2
        return my_list
