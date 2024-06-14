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
        if self.power is not None:
            print(f'Your Power is {self.power} Watts')
        if self.resistance is not None:
            print(f'Your Resistance is {self.resistance} Ohms')
        if self.current is not None:
            print(f'Your Current is {self.current} Amps')
        if self.voltage is None and self.power is None and self.resistance is None and self.current is None:
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
            raise ValueError("Current and Voltage must be provided to calculate power.")

    def R_Times_I_Squared(self):
        if self.current is not None and self.resistance is not None:
            self.power = ((self.current ** 2) * self.resistance)
            self.return_val()
        else:
            raise ValueError("Resistance and Current must be provided to calculate power.")

    def V_Squared_Over_R(self):
        if self.voltage is not None and self.resistance is not None:
            self.power = (self.voltage ** 2) / self.resistance
            self.return_val()
        else:
            raise ValueError("Voltage and resistance must be provided to calculate power.")

class Current(Characteristics):
    def SQRT_P_Over_R(self):
        if self.resistance is not None and self.power is not None:
            self.current = (self.power / self.resistance) ** (1/2)
            self.return_val()
        else:
            raise ValueError("Power and resistance must be provided to calculate current.")
        
    def P_Over_V(self):
        if self.power is not None and self.voltage is not None:
            self.current = (self.power / self.voltage)
            self.return_val()
        else:
            raise ValueError("Power and Voltage must be provided to calculate current.")

    def V_Over_R(self):
        if self.voltage is not None and self.resistance is not None:
            self.current = self.voltage / self.resistance
            self.return_val()
        else:
            raise ValueError("Voltage and Resistance must be provided to calculate current.")

class Resistance(Characteristics): 
    def V_Over_I(self):
        if self.current is not None and self.voltage is not None:
            self.resistance = (self.voltage / self.current)
            self.return_val()
        else:
            raise ValueError("Current and Voltage must be provided to calculate resistance.")

    def V_Squared_Over_P(self):
        if self.voltage is not None and self.power is not None:
            self.resistance = (self.voltage ** 2) / self.power
            self.return_val()
        else:
            raise ValueError("Voltage and Power must be provided to calculate resistance.")

    def IR(self):
        if self.current is not None and self.power is not None:
            self.resistance = self.power / (self.current ** 2)
            self.return_val()
        else:
            raise ValueError("Power and Current must be provided to calculate resistance.")

def clear_screen():
    print("\n" * 50)

def parse_input(input_str):
    try:
        return float(input_str) if input_str else None
    except ValueError:
        return None

def get_user_input(exclude=None):
    voltage = parse_input(input("Enter Voltage (V) if known: ")) if exclude != 'voltage' else None
    current = parse_input(input("Enter Current (I) if known: ")) if exclude != 'current' else None
    resistance = parse_input(input("Enter Resistance (R) if known: ")) if exclude != 'resistance' else None
    power = parse_input(input("Enter Power (P) if known: ")) if exclude != 'power' else None
    return voltage, current, resistance, power

def ohms_law_menu():
    print("Select calculation:")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. Return to Main Menu ")
    choice = int(input("Enter your choice: "))
    clear_screen()
    return choice

def OLMain():
    while True:
        choice = ohms_law_menu()

        if choice == 1:
            print("Calculating Voltage. Please provide Current (I) and Resistance (R) or Power (P).")
            voltage, current, resistance, power = get_user_input(exclude='voltage')
            volt_calc = Voltage(power=power, current=current, resistance=resistance)
            if power is not None and current is not None:
                volt_calc.P_Over_I()
            elif power is not None and resistance is not None:
                volt_calc.SQRT_PR()
            elif current is not None and resistance is not None:
                volt_calc.I_Times_R()
            else:
                print("Not enough information to calculate Voltage.")

        elif choice == 2:
            print("Calculating Current. Please provide Voltage (V) and Resistance (R) or Power (P).")
            voltage, current, resistance, power = get_user_input(exclude='current')
            current_calc = Current(voltage=voltage, power=power, resistance=resistance)
            if power is not None and resistance is not None:
                current_calc.SQRT_P_Over_R()
            elif power is not None and voltage is not None:
                current_calc.P_Over_V()
            elif voltage is not None and resistance is not None:
                current_calc.V_Over_R()
            else:
                print("Not enough information to calculate Current.")

        elif choice == 3:
            print("Calculating Resistance. Please provide Voltage (V) and Current (I) or Power (P).")
            voltage, current, resistance, power = get_user_input(exclude='resistance')
            resistance_calc = Resistance(voltage=voltage, power=power, current=current)
            if voltage is not None and current is not None:
                resistance_calc.V_Over_I()
            elif voltage is not None and power is not None:
                resistance_calc.V_Squared_Over_P()
            elif power is not None and current is not None:
                resistance_calc.IR()
            else:
                print("Not enough information to calculate Resistance.")

        elif choice == 4:
            print("Calculating Power. Please provide Voltage (V) and Current (I) or Resistance (R).")
            voltage, current, resistance, power = get_user_input(exclude='power')
            power_calc = Power(voltage=voltage, current=current, resistance=resistance)
            if voltage is not None and current is not None:
                power_calc.V_Times_I()
            elif current is not None and resistance is not None:
                power_calc.R_Times_I_Squared()
            elif voltage is not None and resistance is not None:
                power_calc.V_Squared_Over_R()
            else:
                print("Not enough information to calculate Power.")

        elif choice == 5:
            print("Returning to Main Menu")
            break
        next_calculation = int(input("Do you want to perform another calculation? Yes (1) / No (0): "))
        if next_calculation == 0:
            break

if __name__ == "__main__":
    OLMain()