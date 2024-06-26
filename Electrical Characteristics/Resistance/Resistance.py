from ResistanceMethods import Resistance,Impedance
from typing import Optional, Tuple
def clear_screen() -> None:
    print("\n" * 50)

def parse_input(input_str: str) -> Optional[float]:
    try:
        return float(input_str) if input_str else None
    except ValueError:
        return None

def get_user_input(exclude: Optional[str] = None) -> Tuple[Optional[float], Optional[float]]:
    resistance1: Optional[float] = parse_input(input("Enter Resistance 1 (R1) if known: ")) if exclude != 'resistance1' else None
    resistance2: Optional[float] = parse_input(input("Enter Resistance 2 (R2) if known: ")) if exclude != 'resistance2' else None
    return resistance1, resistance2

def rz_menu() -> int:
    print("Select calculation:")
    print("1. Calculate Total Resistance (Series)")
    print("2. Calculate Resistance over Branches")
    print("3. Calculate Resistance over Sum Reciprocal")
    print("4. Calculate Resistance Product over Sum")
    print("5. Calculate Total Impedance (Parallel)")
    print("6. Return to Main Menu")
    choice: int = int(input("Enter your choice: "))
    clear_screen()
    return choice

def RZMain() -> None:
    while True:
        choice: int = rz_menu()

        if choice == 1:
            print("Calculating Total Resistance (Series). Please provide both resistances.")
            resistance1, resistance2 = get_user_input()
            res_calc = Resistance(resistance1=resistance1, resistance2=resistance2)
            res_calc.Total_Resistance_Series()

        elif choice == 2:
            print("Calculating Resistance over Branches. Please provide both resistances.")
            resistance1, resistance2 = get_user_input()
            res_calc = Resistance(resistance1=resistance1, resistance2=resistance2)
            res_calc.Resistance_over_branches()

        elif choice == 3:
            print("Calculating Resistance over Sum Reciprocal. Please provide both resistances.")
            resistance1, resistance2 = get_user_input()
            res_calc = Resistance(resistance1=resistance1, resistance2=resistance2)
            res_calc.Resistance_over_SumReciprocal()

        elif choice == 4:
            print("Calculating Resistance Product over Sum. Please provide both resistances.")
            resistance1, resistance2 = get_user_input()
            res_calc = Resistance(resistance1=resistance1, resistance2=resistance2)
            res_calc.Resistance_Prod_Div_Sum()

        elif choice == 5:
            print("Calculating Total Impedance (Parallel). Please provide both impedances.")
            impedance1, impedance2 = get_user_input()
            imp_calc = Impedance(resistance1=impedance1, resistance2=impedance2)
            imp_calc.Total_Impedance_Parallel()

        elif choice == 6:
            print("Returning to Main Menu")
            break

        next_calculation: int = int(input("Do you want to perform another calculation? Yes (1) / No (0): "))
        if next_calculation == 0:
            break

if __name__ == "__main__":
    RZMain()