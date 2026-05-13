#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = list(map(lambda r: replace if r == search else r, my_list))
    return my_list
