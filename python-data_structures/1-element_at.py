#!/usr/bin/python3
def element_at(my_list, idx):
    if __name__ == "__main__":
        if 0 <= idx < len(my_list):
            print('Element at index {} is {}'.format(idx, my_list[idx]))
        else:
            print('Element at index {} is None'.format(idx))
