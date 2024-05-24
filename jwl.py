'''
Author: Donald Jackson
Date: 05/23/2024
Language / File: main.py
Desc: Calculations for Resistance and Impedance Combination in Circuit Analysis
'''




import cmath as c
import main as m

def jwl():
    print("")
    l = float(input("Input Inductance: "))
    print("")
    w = float(input("Input Radial Frequency: "))
    print("")
    ANS = complex((1j * w * l))
    print(complex(ANS))
    return ANS

def jwc():
    print("")
    c = float(input("Input Capacitance: "))
    print("")
    w = float(input("Input Radial Frequency: "))
    print("")
    ANS = complex((1/(1j * w * c)))
    print(complex(ANS))
    return ANS

def mainJW():
    if option == 1:
        jwc()
    elif option == 2:
        jwl()
    else:
        m.main()
        
option = int(input("1 for 1/JWC or 2 for JWL or 3 to return to main menu"))
mainJW()