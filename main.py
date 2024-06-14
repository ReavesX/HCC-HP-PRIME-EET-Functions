'''
Author: Donald Jackson
Date: 05/23/2024
Language / File: main.py
Desc: Calculations for Resistance and Impedance Combination in Circuit Analysis
'''
import OhmsLaw



# Main
def main():
    option = int(input("  1. for Ohms Law\n  2. for Resistance\n  3. for JWL/JWC\n  4. for BJTs\n  5. for 555timer\n "))
             
    if option == 1:
        OhmsLaw.OLMain()
    elif option == 2:
        pass
    elif option == 3: 
        pass
    elif option == 4:
        pass
    elif option == 5: 
        pass


if __name__ == "__main__":
    main()