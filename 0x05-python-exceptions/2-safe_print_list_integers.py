#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k, j = 0, 0
    while k < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            j += 1
        except (ValueError, TypeError):
            pass
        k += 1
    print()
    return j
