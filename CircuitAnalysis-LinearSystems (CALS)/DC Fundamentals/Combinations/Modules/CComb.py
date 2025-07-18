
from menu import create_dropdown_menu, display_and_store_result,create_dialog
import hpprime as h

def CComb_menu():
    h.eval('print')  # Clear terminal
    selection = create_dropdown_menu(
        "Capacitance Combination",
        "C Series",
        "C Parallel",
        "",
        "",
        "Cancel"
    )

    if selection == 5 or selection == 0:
        return  # User cancelled

    # Option 1: series capacitance 1 / ((1/C1) + (1/C2))
    if selection == 1:
        data = create_dialog(
            2, "Capacitance (Series by [1 / ((1/C1) + (1/C2))])",
            "pF", "nF", "µF",
            "pF", "nF", "µF",
            known_value1_label="Capacitance 1:",
            known_value2_label="Capacitance 2:"
        )
        if data is None:
            return
        T, U, B, V, _ = data


        # Convert units
        capacitance_1 = T * (1e-12 if U == 1 else 1e-9 if U == 2 else 1e-6)
        capacitance_2 = B * (1e-12 if V == 1 else 1e-9 if V == 2 else 1e-6)

        # Calculate series total capacitance:
        total_capacitance = 1 / ((1/capacitance_1) + (1/capacitance_2))
        display_and_store_result("Capacitance", total_capacitance)

    # Option 2: Parallel Capacitance C1 + C2
    elif selection == 2:
        data = create_dialog(
            2, "Capacitance (Parallel by [C1 + C2])",
            "pF", "nF", "µF",
            "pF", "nF", "µF",
            known_value1_label="Capacitance 1:",
            known_value2_label="Capacitance 2:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        capacitance_1 = T * (1e-12 if U == 1 else 1e-9 if U == 2 else 1e-6)
        capacitance_2 = B * (1e-12 if V == 1 else 1e-9 if V == 2 else 1e-6)

        total_capacitance = capacitance_1 + capacitance_2
        display_and_store_result("Capacitance:", total_capacitance)