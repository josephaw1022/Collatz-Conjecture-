import math

def count(integer):
    """Counts the number of binary digits representing the integer"""
    digits=0
    while integer>=16:
        digits+=4
        integer/=16
    if integer>7:
        return digits+4
    elif integer>3:
        return digits+3
    elif integer>1:
        return digits+2
    elif integer>0:
        return digits+1
    else:
        return digits

def countdown(integer):
    """Counts the number of initial binary digits of the integer that are 0's"""
    digits=0
    stopper=False
    while integer>=16 and stopper!=True:
        Dhelp = integer%16
        if Dhelp==0:
            digits+=4
        elif Dhelp%8==0:
            digits+=3
            stopper=True
        elif Dhelp%4==0:
            digits+=2
            stopper=True
        elif Dhelp%2==0:
            digits+=1
            stopper=True
        else:
            stopper=True
        integer/=16
    return digits
