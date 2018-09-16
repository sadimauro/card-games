#!/usr/bin/python3

def str_items(items, indent=0, width=0):
    retstr = ''
    
    if not items or len(items) <= 0:
        return ''
    
    count = 0 
    retstr += (indent*' ')
    for item in items:
        retstr += item.__str__()
        count += 1
        if count == width:
            retstr += '\n' + (indent*' ')
            count = 0

    return retstr

def print_items(items, indent=0, width=0):
    if not items or len(items) <= 0:
        return
    
    count = 0
    print(indent*' ', end='')
    for item in items:
        item.print()
        count += 1
        if count == width:
            print('\n', end='')
            print(indent*' ', end='')
            count = 0
