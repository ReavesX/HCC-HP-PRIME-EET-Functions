import MENU as m
import hpprime as h
import CComb as CC
import RComb as RS
import LComb as LS


def combos_main(): 
    while True:
            # Show button-based menu
            choice = m.create_button_menu("Resistance", "Inductors", "Capacitors", "", "")

            if choice == 0:
                m.screenClear()
                h.eval('print("Not implemented yet.")')
                h.eval('wait(2)')
                m.screenClear()
            elif choice == 1:
                m.screenClear()
                h.eval('print("Not implemented yet.")')
                h.eval('wait(2)')
                m.screenClear()
            elif choice == 2:
                m.screenClear()
                h.eval('print("Not implemented yet.")')
                h.eval('wait(2)')
                m.screenClear()
            elif choice == 3 or choice == 4 or choice == 5:
                # Exit
                m.screenClear()
                h.eval('print("Goodbye!")')
                break
            else:
                # Soft key press that wasn't mapped
                m.screenClear()
                h.eval('print("Invalid selection.")')
                h.eval('wait(2)')
                m.screenClear()
