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
    option = int(input('''1. for Ohms Law\n
                          2. for Resistance\n
                          3. for JWL/JWC\n
                          4. for BJTs\n
                          5. for 555timer\n '''))
             
    if option == 1:
        OL.main()
    elif option == 2:
        RZ.main()
    elif option == 3: 
        JWL.jwMain()
    elif option == 4:
        bjt.main()
    elif option == 5: 
        tmr.tmrMain()


main()