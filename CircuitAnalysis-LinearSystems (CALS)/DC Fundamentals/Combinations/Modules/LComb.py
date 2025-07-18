
from menu import create_dropdown_menu, display_and_store_result,create_dialog
import hpprime as h

def LComb_menu():
    h.eval('print')  # Clear terminal
    selection = create_dropdown_menu(
        "Inductor Combination",
        "L Series",
        "L Parallel",
        "",
        "",
        "Cancel"
    )

    if selection == 5 or selection == 0:
        return  # User cancelled

    # Option 1: series incudctance L1+L2
    if selection == 1:
        data = create_dialog(
            2, "Inductance (Series by L1 + L2 )",
            "nH", "µH", "mH",
            "nH", "µH", "mH",
            known_value1_label="Inductance 1:",
            known_value2_label="Inductance 2:"
        )
        if data is None:
            return
        T, U, B, V, _ = data


        # Convert units
        inductance_1 = T * (1e-9 if U == 1 else 1e-6 if U == 2 else 1e-3)
        inductance_2 = B * (1e-9 if V == 1 else 1e-6 if V == 2 else 1e-3)

        # Calculate series total capacitance:
        total_inductance = inductance_1 + inductance_2
        display_and_store_result("Inductance:", total_inductance)

    # Option 2: Parallel Inductance 1 / ((1/L1) + (1/L2))
    elif selection == 2:
        data = create_dialog(
            2, "Inductance (Parallel by [1 / ((1/L1) + (1/L2))])",
            "nH", "µH", "mH",
            "nH", "µH", "mH",
            known_value1_label="Inductance 1:",
            known_value2_label="Inductance 2:"
        )
        if data is None:
            return
        T, U, B, V, _ = data

        inductance_1 = T * (1e-9 if U == 1 else 1e-6 if U == 2 else 1e-3)
        inductance_2 = B * (1e-9 if V == 1 else 1e-6 if V == 2 else 1e-3)

        total_inductance = 1 / ((1/inductance_1) + (1/inductance_2))
        display_and_store_result("Inductance:", total_inductance)