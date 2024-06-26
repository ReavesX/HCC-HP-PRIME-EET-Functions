'''
Author: Donald Jackson
Date: 06/14/2024
Language / File: ResistanceImpedance.py
Desc: Calculations for Resistance and Impedance Combination in Circuit Analysis
'''

import cmath as c
from typing import Optional, Tuple
class Resistance:
    def __init__(self, resistance1=None, resistance2=None, result=None):
        self.resistance1 = resistance1  # Can be float or complex
        self.resistance2 = resistance2  # Can be float or complex
        self.result = result            # Result as float or complex

    def return_val(self):
        # Check if result is a complex number
        if self.result is not None:
            if isinstance(self.result, complex):
                print(f'Your impedance in rectangular form: {self.result.real} + {self.result.imag}j Ohms')
                magnitude, angle = self.convert_to_polar(self.result)
                print(f'Your impedance in polar form: {magnitude} Ohms ∠ {angle}°')
            else:
                print(f'Your resistance is {self.result} Ohms')
        else:
            print('Calculation not available.')

    def convert_to_polar(self, z):
        # Convert complex number to polar form (magnitude and phase angle in degrees)
        magnitude = abs(z)
        angle = c.phase(z) * (180 / c.pi)  
        return magnitude, angle

    def Total_Resistance_Series(self):
        if self.resistance1 is not None and self.resistance2 is not None:
            self.result = self.resistance1 + self.resistance2
            self.return_val()

    def Resistance_over_branches(self):
        if self.resistance1 and self.resistance2:
            self.result = self.resistance1 / 2
            self.return_val()

    def Resistance_over_SumReciprocal(self):
        if self.resistance1 and self.resistance2:
            self.result = 1 / ((1 / self.resistance1) + (1 / self.resistance2))
            self.return_val()

    def Resistance_Prod_Div_Sum(self):
        if self.resistance1 and self.resistance2:
            self.result = (self.resistance1 * self.resistance2) / (self.resistance1 + self.resistance2)
            self.return_val()

class Impedance(Resistance):
    # Inherit from Resistance and add methods for handling complex impedance

    def Total_Impedance_Parallel(self):
        if self.resistance1 is not None and self.resistance2 is not None:
            self.result = 1 / ((1 / self.resistance1) + (1 / self.resistance2))
            self.return_val()

    def Impedance_with_Phase(self, magnitude1, phase1, magnitude2, phase2):
        # Calculate impedance using magnitudes and phase angles
        if magnitude1 is not None and phase1 is not None and magnitude2 is not None and phase2 is not None:
            z1 = c.rect(magnitude1, c.radians(phase1))  # Convert magnitude and phase to complex
            z2 = c.rect(magnitude2, c.radians(phase2))
            self.resistance1 = z1
            self.resistance2 = z2
            self.Total_Impedance_Series()