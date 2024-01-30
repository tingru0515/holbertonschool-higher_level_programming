#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0
            if type(element_1) not in (int, float) or type(element_2) not in (int, float):
                print("wrong type")
                result = 0
            else:
                result = element_1 / element_2
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    if len(my_list_1) != len(my_list_2):
        print("out of range")
    return result_list
