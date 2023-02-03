#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''

    evenlist = range(n+1)
    evenlist = filter(lambda m: m % 2 == 0, evenlist)
    return list(evenlist)
