import MENU as m
import hpprime as h
import voltage as v
import resistance as r
import power as p
import current as c

def ohmslaw_main(): 
    while True:
            # Show button-based menu
            choice = m.create_button_menu("Voltage", "Current", "Resistance", "Power", "Exit")

            if choice == 0:
                v.voltage_menu()
            elif choice == 1:
                c.current_m()
            elif choice == 2:
                r.resistance_menu()
            elif choice == 3:
                p.power_menu()
            elif choice == 4:  # Exit
                m.screenClear()
                h.eval('print("Goodbye!")')
                break
            else:
                # Soft key press that wasn't mapped
                m.screenClear()
                h.eval('print("Invalid selection.")')
                h.eval('wait(2)')
                m.screenClear()
