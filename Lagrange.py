from colorama import Fore

def Dispenser(tmp):
    if(type(tmp) is not str): raise TypeError
    array = tmp.split() 
    for c in range(array.__len__()):
        array[c] = float(array[c])
    return array

def Lagrange(XPoints, YPoints, X):
    DesiredValue = 0
    L = 1
    for c in range(len(YPoints)):
        for p in range(len(XPoints)):
            if(c == p): continue
            L *= (X - XPoints[p])/(XPoints[c] - XPoints[p])
        DesiredValue += YPoints[c] * L
        L = 1
    return DesiredValue   

tmp = input('Enter X points: ' + Fore.GREEN)
KnownPoints = Dispenser(tmp)
tmp = input(Fore.RESET + 'Enter function values in these points: ' + Fore.GREEN)
ValuesInPoints = Dispenser(tmp)
XToBeFound = float(input(Fore.RESET + 'Enter X in which you want to get function value: '+ Fore.GREEN))

if(len(KnownPoints) != len(ValuesInPoints)):
    raise RuntimeError
print(f'{Fore.RESET}Function value in x = {XToBeFound} is {Fore.GREEN}{Lagrange(KnownPoints, ValuesInPoints, XToBeFound)}{Fore.RESET}')