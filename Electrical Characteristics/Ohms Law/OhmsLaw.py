from OhmsLawMethods import Resistance,Current,Voltage,Power
from typing import Optional,Tuple


def clear_screen() -> None:
    print("\n" * 50)

def parse_input(input_str: str) -> Optional[float]:
    try:
        return float(input_str) if input_str else None
    except ValueError:
        return None

def get_user_input(exclude: Optional[str] = None) -> Tuple[Optional[float], Optional[float], Optional[float], Optional[float]]:
    voltage: Optional[float] = parse_input(input("Enter Voltage (V) if known: ")) if exclude != 'voltage' else None
    current: Optional[float] = parse_input(input("Enter Current (I) if known: ")) if exclude != 'current' else None
    resistance: Optional[float] = parse_input(input("Enter Resistance (R) if known: ")) if exclude != 'resistance' else None
    power: Optional[float] = parse_input(input("Enter Power (P) if known: ")) if exclude != 'power' else None
    return voltage, current, resistance, power

def ohms_law_menu() -> int:
    print("Select calculation:")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. Return to Main Menu")
    choice: int = int(input("Enter your choice: "))
    clear_screen()
    return choice


def OLMain() -> None:
    while True:
        choice: int = ohms_law_menu()

        if choice == 1:
            print("Calculating Voltage. Please provide Current (I) and Resistance (R) or Power (P).")
            voltage, current, resistance, power = get_user_input(exclude='voltage')
            volt_calc = Voltage(power=power, current=current, resistance=resistance)
            if current is not None and resistance is not None:
                volt_calc.I_Times_R()
            elif power is not None and current is not None:
                volt_calc.P_Over_I()
            elif power is not None and resistance is not None:
                volt_calc.SQRT_PR()
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

        next_calculation: int = int(input("Do you want to perform another calculation? Yes (1) / No (0): "))
        if next_calculation == 0:
            break

if __name__ == "__main__":
    OLMain()