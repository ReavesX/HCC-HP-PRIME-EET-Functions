from math import sqrt
import hpprime as h
from MENU import create_dialog, create_dropdown_menu, display_and_store_result


def voltage_menu():
    h.eval('print')  # Clear terminal
    selection = create_dropdown_menu(
        "Voltage Calculation",
        "IR",
        "P/I",
        "SQRT(PR)",
        "",
        "Cancel"
    )

    if selection == 5 or selection == 0:
        return  # User cancelled

    # Option 1: Voltage = I * R
    if selection == 1:
        data = create_dialog(
            2, "Voltage (V = IR)",
            "uA", "mA", "A",
            "Ohm", "Kilo-Ohm", "Mega-Ohm",
            known_value1_label="Current:",
            known_value2_label="Resistance/Impedance:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        # Convert units
        current = T * (1e-6 if U == 1 else 1e-3 if U == 2 else 1)
        resistance = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)
        voltage = current * resistance
        display_and_store_result("Voltage", voltage)

    # Option 2: Voltage = Power / Current
    elif selection == 2:
        data = create_dialog(
            2, "Voltage (V = P / I)",
            "uA", "mA", "A",
            "Watt", "kW", "MW",
            known_value1_label="Current:",
            known_value2_label="Power:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        current = T * (1e-6 if U == 1 else 1e-3 if U == 2 else 1)
        power = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)
        voltage = power / current
        display_and_store_result("Voltage", voltage)

    # Option 3: Voltage = sqrt(P * R)
    elif selection == 3:
        data = create_dialog(
            2, "Voltage (V = √(P × R))",
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
        voltage = sqrt(power * resistance)
        display_and_store_result("Voltage", voltage)

    else:
        h.eval('print("Invalid selection.")')
