#!/usr/bin/python3
def no_c(my_string):
    newstring = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return ("".join(newstring))
