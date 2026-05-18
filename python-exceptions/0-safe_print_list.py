#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try: print("{}".format(my_list[:x]))
    except: print("{}".format(my_list[:len(my_list)]))
