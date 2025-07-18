
from menu import create_dropdown_menu, display_and_store_result,create_dialog
import hpprime as h

def RComb_menu():
    h.eval('print')  # Clear terminal
    selection = create_dropdown_menu(
        "Resistor Combination",
        "R Series",
        "R Parallel",
        "",
        "",
        "Cancel"
    )

    if selection == 5 or selection == 0:
        return  # User cancelled

    # Option 1: series resistance
    if selection == 1:
        data = create_dialog(
            2, "Resistance (Series by R1 + R2)",
            "Ω", "KΩ", "MΩ",
            "Ω", "KΩ", "MΩ",
            known_value1_label="Resistance 1:",
            known_value2_label="Resistance 2:"
        )
        if data is None:
            return
        T, U, B, V, _ = data


        # Convert units
        resistance_1 = T * (1 if U == 1 else 1e3 if U == 2 else 1e6)
        resistance_2 = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)

        # Calculate series total capacitance:
        total_resistance = resistance_1 + resistance_2
        display_and_store_result("Resistance:", total_resistance)

    # Option 2: Parallel resistance
    elif selection == 2:
        data = create_dialog(
            2, "Resistance (Parallel by 1/[(1/R1) + (1/R2)])",
            "Ω", "KΩ", "MΩ",
            "Ω", "KΩ", "MΩ",
            known_value1_label="Resistance 1:",
            known_value2_label="Resistance 2:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        resistance_1 = T * (1 if U == 1 else 1e3 if U == 2 else 1e6)
        resistance_2 = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)

        total_resistance = 1 / ((1/resistance_1) + (1/resistance_2))
        display_and_store_result("Resistance:", total_resistance)