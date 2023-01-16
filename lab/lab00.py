# DSC 20 Lab 00
# Name: Zehui Zhang
# PID:  A16151490

def name_sum(firstName, lastName):
    """
    Write a Python program to sum up the lengths of two given names. 
    However, if the sum is strictly greater than 15, return only the 
    length of the firstName. If the sum is less than 10, return my 
    name as a string: "Marina".

    >>> name_sum("Marina", "Langlois")
    14
    >>> name_sum("Elvy", "Chen")
    'Marina'
    >>> name_sum("Kiefer", "Sutherland")
    6
    """
    F = len(firstName)
    L = len(lastName)
    if F+L >15:
        return F
    elif F+L < 10:
        return 'Marina'
    else:
        return F+L
