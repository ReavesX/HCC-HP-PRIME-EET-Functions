# HP Prime G2 HCC EET Programs
# Author: Donald Jackson
# Lang: Micropython
# This program performs the various functions necessary for completing the AA and AS CpE and EE Tracks  
# at Hillsborough Community College

import cmath



def optionTree():
    print("1: JWL", "") # option 1 is J*W*L
    print("2: 1/(jwc)","") # option 2 is 1 / (J*W*C)
    print("3: Zt ||") # option 3 is Zp 1/((1/z1)+(1/z2))
    print("4: Exit") # exit case
    userInput = input("Choose a number 1-4")
    
    if int(userInput) == 1:
        jwl()
    elif int(userInput) == 2: 
        jwc()
    elif int(userInput) == 3:
        Zp()
    else:
        return 0 # end option tree 

def jwl():
    print("")
    l = float(input("Input Inducatnce: "))
    print("")
    w = float(input("Input Radial Frequency: "))
    print("")
    outputF = complex((1j * w * l))
    print(complex(outputF))
    return outputF

# Main begins here
optionTree() 