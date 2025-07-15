import MENU as m
import voltage as v
import hpprime as h
# import current, resistance, power — when those are ready

def main():
    m.welcomeScreen()

    while True:
        # Show button-based menu
        choice = m.create_button_menu("Voltage", "Current", "Resistance", "Power", "Exit")

        if choice == 0:
            v.voltage_m()
        elif choice == 1:
            m.screenClear()
            h.eval('print("Current menu not implemented yet.")')
            h.eval('wait(2)')
            m.screenClear()
        elif choice == 2:
            m.screenClear()
            h.eval('print("Resistance menu not implemented yet.")')
            h.eval('wait(2)')
            m.screenClear()
        elif choice == 3:
            m.screenClear()
            h.eval('print("Power menu not implemented yet.")')
            h.eval('wait(2)')
            m.screenClear()
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

# Launch the app
main()