import hpprime as h
from MENU import create_dialog, create_dropdown_menu, display_and_store_result


def resistance_menu():
    h.eval('print')  # Clear terminal
    selection = create_dropdown_menu(
        "Resistance Calculation",
        "V/I",
        "V^2 / P",
        "P / I^2",
        "",
        "Cancel"
    )

    if selection == 5 or selection == 0:
        return  # User cancelled

    # Option 1: Resistance = Voltage / Current
    if selection == 1:
        data = create_dialog(
            2, "Resistance (R = V / I)",
            "mV", "V", "kV",
            "uA", "mA", "A",
            known_value1_label="Voltage:",
            known_value2_label="Current:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        # Convert units
        voltage = T * (1e-3 if U == 1 else 1 if U == 2 else 1e3)
        current = B * (1e-6 if V == 1 else 1e-3 if V == 2 else 1)
        
        resistance = voltage / current
        display_and_store_result("Resistance", resistance)

    # Option 2: Resistance = Voltage^2 / Power
    elif selection == 2:
        data = create_dialog(
            2, "Resistance (R = V^2 / P)",
            "mV", "V", "kV",
            "W", "kW", "MW",
            known_value1_label="Voltage:",
            known_value2_label="Power:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        voltage = T * (1e-3 if U == 1 else 1 if U == 2 else 1e3)
        power = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)

        resistance = (voltage**2) / power
        display_and_store_result("Resistance", resistance)

    # Option 3: Resistance = Power / Current^2
    elif selection == 3:
        data = create_dialog(
            2, "Resistance (R = P / I^2)",
            "W", "kW", "MW",
            "uA", "mA", "A",
            known_value1_label="Power:",
            known_value2_label="Current:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        power = T * (1 if U == 1 else 1e3 if U == 2 else 1e6)
        current = B * (1e-6 if V == 1 else 1e-3 if V == 2 else 1)

            
        resistance = power / (current**2)
        display_and_store_result("Resistance", resistance)

    else:
        h.eval('print("Invalid selection.")')

