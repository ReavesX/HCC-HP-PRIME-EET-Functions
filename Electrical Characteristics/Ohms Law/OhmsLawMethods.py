from typing import Optional, Tuple

# Base class for Characteristics
class Characteristics:
    def __init__(self, power: Optional[float] = None, current: Optional[float] = None, resistance: Optional[float] = None, voltage: Optional[float] = None):
        self.power: Optional[float] = power
        self.current: Optional[float] = current
        self.resistance: Optional[float] = resistance
        self.voltage: Optional[float] = voltage

    def return_val(self) -> None:
        if self.voltage is not None:
            print(f'Your Voltage is {self.voltage} Volts')
        if self.power is not None:
            print(f'Your Power is {self.power} Watts')
        if self.resistance is not None:
            print(f'Your Resistance is {self.resistance} Ohms')
        if self.current is not None:
            print(f'Your Current is {self.current} Amps')
        if self.voltage is None and self.power is None and self.resistance is None and self.current is None:
            print('Calculation not available.')

# Derived classes for specific calculations
class Voltage(Characteristics):
    def P_Over_I(self) -> None:
        if self.power is not None and self.current is not None:
            self.voltage = self.power / self.current
            self.return_val()
        else:
            raise ValueError("Power and current must be provided to calculate voltage.")

    def SQRT_PR(self) -> None:
        if self.power is not None and self.resistance is not None:
            self.voltage = (self.power * self.resistance) ** 0.5
            self.return_val()
        else:
            raise ValueError("Power and resistance must be provided to calculate voltage.")

    def I_Times_R(self) -> None:
        if self.current is not None and self.resistance is not None:
            self.voltage = self.current * self.resistance
            self.return_val()
        else:
            raise ValueError("Current and resistance must be provided to calculate voltage.")

class Power(Characteristics):
    def V_Times_I(self) -> None:
        if self.voltage is not None and self.current is not None:
            self.power = self.voltage * self.current
            self.return_val()
        else:
            raise ValueError("Current and Voltage must be provided to calculate power.")

    def R_Times_I_Squared(self) -> None:
        if self.current is not None and self.resistance is not None:
            self.power = ((self.current ** 2) * self.resistance)
            self.return_val()
        else:
            raise ValueError("Resistance and Current must be provided to calculate power.")

    def V_Squared_Over_R(self) -> None:
        if self.voltage is not None and self.resistance is not None:
            self.power = (self.voltage ** 2) / self.resistance
            self.return_val()
        else:
            raise ValueError("Voltage and resistance must be provided to calculate power.")

class Current(Characteristics):
    def SQRT_P_Over_R(self) -> None:
        if self.resistance is not None and self.power is not None:
            self.current = (self.power / self.resistance) ** 0.5
            self.return_val()
        else:
            raise ValueError("Power and resistance must be provided to calculate current.")
        
    def P_Over_V(self) -> None:
        if self.power is not None and self.voltage is not None:
            self.current = self.power / self.voltage
            self.return_val()
        else:
            raise ValueError("Power and Voltage must be provided to calculate current.")

    def V_Over_R(self) -> None:
        if self.voltage is not None and self.resistance is not None:
            self.current = self.voltage / self.resistance
            self.return_val()
        else:
            raise ValueError("Voltage and Resistance must be provided to calculate current.")

class Resistance(Characteristics): 
    def V_Over_I(self) -> None:
        if self.current is not None and self.voltage is not None:
            self.resistance = self.voltage / self.current
            self.return_val()
        else:
            raise ValueError("Current and Voltage must be provided to calculate resistance.")

    def V_Squared_Over_P(self) -> None:
        if self.voltage is not None and self.power is not None:
            self.resistance = (self.voltage ** 2) / self.power
            self.return_val()
        else:
            raise ValueError("Voltage and Power must be provided to calculate resistance.")

    def IR(self) -> None:
        if self.current is not None and self.power is not None:
            self.resistance = self.power / (self.current ** 2)
            self.return_val()
        else:
            raise ValueError("Power and Current must be provided to calculate resistance.")