import MENU as m
import hpprime as h
from  CComb import CComb_menu
from  RComb import RComb_menu
from  LComb import LComb_menu


def combos_main(): 
    while True:
            # Show button-based menu
            choice = m.create_button_menu("Resistance", "Inductors", "Capacitors", "", "")

            if choice == 0:
                RComb_menu()
            elif choice == 1:
                LComb_menu()
            elif choice == 2:
                CComb_menu()
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
