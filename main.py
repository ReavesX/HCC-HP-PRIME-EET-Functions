'''
Author: Donald Jackson
Date: 05/23/2024
Language / File: main.py
Desc: Calculations for Resistance and Impedance Combination in Circuit Analysis
'''


import jwl as jwl
import tmr_555 as tmr
import OhmsLaw as OL
import Resistance as RZ
import BJTs as bjt



# Main
def main():
    option = int(input('''1 for Ohms Law, 2 for Resistance,
                          3 for JWL/JWC, 4 for Bjts,
                          5 for 555timer '''))
             
    if option == 1:
        OL.main()
    elif option == 2:
        RZ.main()
    elif option == 3: 
        JWL.main()
    elif option == 4:
        bjt.main()
    elif option == 5: 
        tmr.main()


main()