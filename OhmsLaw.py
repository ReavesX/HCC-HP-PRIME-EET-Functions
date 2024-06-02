'''
Author: Donald Jackson
Date: 05/23/2024
Language / File: OhmsLaw.py
Desc: Calculations for Ohms Law
'''

import cmath as c

class Characteristics:
    def __init__(self, power=None, current=None, resistance=None, voltage=None):
        self.resistance = resistance
        self.current = current
        self.power = power
        self.voltage = voltage
    def return_val(self):
        if self.voltage is not None:
            print(f'Your Voltage is {self.voltage} Volts')
        elif self.power is not None:
            print(f'Your Power is {self.power} Watts')
        elif self.resistance is not None:
            print(f'Your Resistance is {self.resistance} Ohms')
        elif self.current is not None:
            print(f'Your Current is {self.current} Amps')
        else:
            print('Calculation not available.')  
        
class Voltage(Characteristics):
    def P_Over_I(self):
        if self.power is not None and self.current is not None:
            self.voltage = self.power / self.current
            self.return_val()
        else:
            raise ValueError("Power and current must be provided to calculate voltage.")

    def SQRT_PR(self):
        if self.power is not None and self.resistance is not None:
            self.voltage = (self.power * self.resistance) ** 0.5
            self.return_val()
        else:
            raise ValueError("Power and resistance must be provided to calculate voltage.")

    def I_Times_R(self):
        if self.current is not None and self.resistance is not None:
            self.voltage = self.current * self.resistance
            self.return_val()
        else:
            raise ValueError("Current and resistance must be provided to calculate voltage.")
   
class Power(Characteristics):
    def V_Times_I(self):
        if self.voltage is not None and self.current is not None:
            self.power = self.voltage * self.current
            self.return_val()
        else:
            raise ValueError("Current and Voltage must be provided to calculate Power.")

    def R_Times_I_Squared(self):
        if self.current is not None and self.resistance is not None:
            self.power = ((self.current ** 2) * self.resistance)
            self.return_val()
        else:
            raise ValueError("Resistance and Current must be provided to calculate Power.")

    def V_Squared_Over_R(self):
        if self.voltage is not None and self.resistance is not None:
            self.power = (self.voltage ** 2) / self.resistance
            self.return_val()
        else:
            raise ValueError("Voltage and resistance must be provided to calculate Power.")

class Current(Characteristics):
    def SQRT_P_Over_R(self):
        if self.resistance is not None and self.power is not None:
            self.current = (self.power / self.resistance) ** (1/2)
            self.return_val()
        else:
            raise ValueError("Power and resistance must be provided to calculate Current.")
        
    def P_Over_V(self):
        if self.power is not None and self.voltage is not None:
            self.current = (self.power / self.voltage)
            self.return_val()
        else:
            raise ValueError("Power and Voltage must be provided to calculate Current.")

    def V_Over_R(self):
        if self.voltage is not None and self.resistance is not None:
            self.current = self.voltage / self.resistance
            self.return_val()
        else:
            raise ValueError("Voltage and Resistance must be provided to calculate Current.")

class Resistance(Characteristics):
    def V_Over_I(self):
        if self.current is not None and self.voltage is not None:
            self.resistance = (self.voltage / self.current)
            self.return_val()
        else:
            raise ValueError("Current and Voltage must be provided to calculate Resistance.")
    def V_Squared_Over_P(self):
        if self.voltage is not None and self.power is not None:
            self.resistance = (self.voltage ** 2) / self.power
            self.return_val()
        else:
            raise ValueError("Voltage and Power must be provided to calculate voltage.")

    def IR(self):
        if self.current is not None and self.power is not None:
            self.resistance = self.power / (self.current ** 2)
            self.return_val()
        else:
            raise ValueError("Power and Current must be provided to calculate voltage.")


"""
def olMain():
    import main as m
    option = int(input("1. Voltage\n2. Power\n3. Current\n4. Resistance\n"))
    if option == 1:
        Voltage()
    elif option == 2:
        Power()
    elif option == 3:
        Current()
    elif option == 4:
        Resistance()
"""