
a=3
try:
    if a<4:
        a=a/(a-3)
except ZeroDivisionError:
    print("Division By Zero Exception")