from math import sqrt
import hpprime as h
from MENU import create_dialog, create_dropdown_menu, display_and_store_result

def current_menu():
    h.eval('print')  # Clear terminal
    selection = create_dropdown_menu(
        "Current Calculation",
        "V/R",
        "P/V",
        "SQRT(P/R)",
        "",
        "Cancel"
    )

    if selection == 5 or selection == 0:
        return  # User cancelled

    # Option 1: Current = Voltage / Resistance
    if selection == 1:
        data = create_dialog(
            2, "Current (I = V / R)",
            "mV", "V", "kV",
            "Ohm", "Kilo-Ohm", "Mega-Ohm",
            known_value1_label="Voltage:",
            known_value2_label="Resistance/Impedance:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        # Convert units
        voltage = T * (1e-3 if U == 1 else 1 if U == 2 else 1e3)
        resistance = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)

        current = voltage / resistance
        display_and_store_result("Current", current)

    # Option 2: Current = Power / Voltage
    elif selection == 2:
        data = create_dialog(
            2, "Current (I = P / V)",
            "W", "kW", "MW",
            "mV", "V", "kV",
            known_value1_label="Power:",
            known_value2_label="Voltage:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        power = T * (1 if U == 1 else 1e3 if U == 2 else 1e6)
        voltage = B * (1e-3 if V == 1 else 1 if V == 2 else 1e3)

        current = power / voltage
        display_and_store_result("Current", current)

    # Option 3: Current = sqrt(Power / Resistance)
    elif selection == 3:
        data = create_dialog(
            2, "Current (I = √(P / R))",
            "W", "kW", "MW",
            "Ohm", "Kilo-Ohm", "Mega-Ohm",
            known_value1_label="Power:",
            known_value2_label="Resistance/Impedance:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        power = T * (1 if U == 1 else 1e3 if U == 2 else 1e6)
        resistance = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)

        current = sqrt(power / resistance)
        display_and_store_result("Current", current)

    else:
        h.eval('print("Invalid selection.")')