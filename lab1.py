# Name:         Dandy Vo
# Course:       CPE 202
# Assignment:   Lab 1
# Instructor:   Hatalsky
# Term:         Spring 2019

def max_list_iter(int_list):
    if int_list == None:
        raise ValueError
    elif len(int_list) == 0:  
        return None

    max_number = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > max_number:
            max_number = int_list[i]
    return max_number   


def reverse_rec(int_list):
    if int_list == None:
        raise ValueError
    elif int_list == []:
        return []
    return reverse_rec(int_list[1:]) + [int_list[0]] 


def bin_search(target, low, high, int_list):  # must use recursion
    if int_list == None:
        raise ValueError
    if low == high and int_list[low] != target:
        return None
    midpoint = int((low + high) / 2)
    if int_list[midpoint] == target:
        return midpoint
    elif int_list[midpoint] > target:
        return bin_search(target, low, midpoint - 1, int_list)
    else:
        return bin_search(target, midpoint + 1, high, int_list)

