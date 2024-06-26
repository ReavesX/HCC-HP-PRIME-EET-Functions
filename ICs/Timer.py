from typing import Optional, Tuple
from TimerMethods import Astable, Monostable

def clear_screen() -> None:
    print("\n" * 50)

def parse_input(input_str: str) -> Optional[float]:
    try:
        return float(input_str) if input_str else None
    except ValueError:
        return None

def get_user_input(exclude: Optional[str] = None) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    r1: Optional[float] = parse_input(input("Enter Resistance 1 (R1) if known: ")) if exclude != 'r1' else None
    r2: Optional[float] = parse_input(input("Enter Resistance 2 (R2) if known: ")) if exclude != 'r2' else None
    c1: Optional[float] = parse_input(input("Enter Capacitance (C1) if known: ")) if exclude != 'c1' else None
    return r1, r2, c1

def timer_menu() -> int:
    print("Select 555 Timer Configuration:")
    print("1. Astable Mode")
    print("2. Monostable Mode")
    print("3. Return to Main Menu")
    choice: int = int(input("Enter your choice: "))
    clear_screen()
    return choice

def TimerMain() -> None:
    while True:
        choice: int = timer_menu()

        if choice == 1:
            print("Selected Astable Mode. Please provide values for R1, R2, and C1 if known.")
            r1, r2, c1 = get_user_input()
            astable_timer = Astable(r1=r1, r2=r2, c1=c1)
            astable_submenu(astable_timer)

        elif choice == 2:
            print("Selected Monostable Mode. Please provide values for R1 and C1 if known.")
            r1, _, c1 = get_user_input(exclude='r2')
            monostable_timer = Monostable(r1=r1, c1=c1)
            monostable_submenu(monostable_timer)

        elif choice == 3:
            print("Returning to Main Menu")
            break

        next_calculation: int = int(input("Do you want to perform another timer configuration? Yes (1) / No (0): "))
        if next_calculation == 0:
            break

def astable_submenu(astable_timer: Astable) -> None:
    while True:
        print("\nSelect calculation for Astable Mode:")
        print("1. Calculate High and Low Times")
        print("2. Calculate Resistances (R1 and R2)")
        print("3. Calculate Frequency")
        print("4. Calculate Capacitance")
        print("5. Return to 555 Timer Menu")
        choice: int = int(input("Enter your choice: "))
        clear_screen()

        if choice == 1:
            try:
                astable_timer.calculate_high_low_times()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            try:
                astable_timer.calculate_resistances()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            try:
                astable_timer.calculate_frequency()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 4:
            try:
                astable_timer.calculate_capacitance()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 5:
            print("Returning to 555 Timer Menu")
            break

        next_calculation: int = int(input("Do you want to perform another calculation in Astable Mode? Yes (1) / No (0): "))
        if next_calculation == 0:
            break

def monostable_submenu(monostable_timer: Monostable) -> None:
    while True:
        print("\nSelect calculation for Monostable Mode:")
        print("1. Calculate Period")
        print("2. Calculate Resistance (R1)")
        print("3. Calculate Capacitance (C1)")
        print("4. Return to 555 Timer Menu")
        choice: int = int(input("Enter your choice: "))
        clear_screen()

        if choice == 1:
            try:
                monostable_timer.calculate_period()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            try:
                monostable_timer.calculate_resistance()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            try:
                monostable_timer.calculate_capacitance()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 4:
            print("Returning to 555 Timer Menu")
            break

        next_calculation: int = int(input("Do you want to perform another calculation in Monostable Mode? Yes (1) / No (0): "))
        if next_calculation == 0:
            break

if __name__ == "__main__":
    TimerMain()