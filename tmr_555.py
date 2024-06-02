'''
Author: Donald Jackson
Date: 05/23/2024
Language / File: 555tmr.py
Desc: Calculations for utilizing the legendary 555 Timer IC
'''

def astable()-> float:
    def  aStableHighLowTimes()-> float:
        R1 = float(input("Input Your Resistor Value "))
        R2 = float(input("Input Your Second Resistor Value "))
        C1 = float(input("Input Your Capacitor Value "))
        THigh = 0.693 * ( R1 + R2 ) * C1
        TLow = 0.693 * R2 * C1
        print(str(THigh)+"Seconds High\n")
        print(str(TLow) +"Seconds Low\n")
        print(f'Seconds High:{THigh}\nSeconds Low:{TLow}')
                            
    def  aStableResistances()-> float:
        THigh= float(input("Input Your High Time"))
        TLow= float(input("Input Your Low Time"))
        C1 = float(input("Input Your Capacitor Value"))       
        R2 =  TLow / ( 0.693 * C1 )
        R1 = (THigh / ( 0.693 * C1 )) - R2
        print(f'R1 is {R1} Ohms\n')
        print(f'R2 is {R2} Ohms\n')
    

    def aStableFrequency()-> float:
        R1 = float(input("Input Your Resistor Value "))
        R2 = float(input("Input Your Second Resistor Value "))
        C1 = float(input("Input Your Capacitor Value "))
        f = 1.44 / ((R1 + (2 * R2))* C1 )
        print(f)
        return f
    def aStableCapacitance()-> float:
        TLow= float(input("Input Your Low Time "))
        R2 = float(input("Input Your Second Resistor Value "))
        C1 = TLow - ( 0.693 * R2 )
        print(C1)
        return C1
    option = int(input("1. High and Low Times\n2. Resistance\n3. Frequency\n4. Capacitance\n5. Return to 555Timer Menu\n"))
    print("\n")
    if option == 1:
        aStableHighLowTimes()
    elif option == 2:
        aStableResistances()
    elif option == 3:
        aStableFrequency()
    elif option == 4:
        aStableCapacitance()
    elif option == 5: 
        tmrMain()

# The following functions calculate characteristics of the monostable 555 Timer Configuration
def monostable() -> float:
    def monoPeriod()-> float: 
        # Function returns the period of operation given the resistance and capacitance
        R1 = float(input("Input Your Resistor Value "))
        C1 = float(input("Input Your Capacitor Value "))
        T = 1.1 * R1 * C1
        print(T)    
        return T   
  

    def monoRes()-> float:
        # Function returns the necessary resistance value for given period and capacitance
        T = float(input("Input Your Period Value "))
        C1 = float(input("Input Your Capacitor Value "))
        R1 = T / (1.1*C1)
        print(R1)       
        return R1
    
   
    def monoCap()-> float:
        # Function returns the necessary capacitance value for a given period and resistance
        T = float(input("Input Your Period Value "))
        R1 = float(input("Input Your Resistor Value "))
        C1 = T / (1.1*R1)
        print(C1)
        return C1
   
    option = int(input("1. Period\n2. Resistance\n3. Capacitance\n4. Return to 555Timer Menu\n "))
    print("\n")
    if option == 1:
        monoPeriod()
    elif option == 2:
        monoRes()
    elif option == 3:
        monoCap()
    elif option == 4:
        tmrMain()
        
def tmrMain():
    import main as m
    from main import main()
    option = int(input("1.Astable\n2.Monostable\n3.Return to main menu\n"))
    print("\n")
    if option == 1:
        astable()
    elif option == 2:
        monostable()
    elif option == 3:
       m.main()
