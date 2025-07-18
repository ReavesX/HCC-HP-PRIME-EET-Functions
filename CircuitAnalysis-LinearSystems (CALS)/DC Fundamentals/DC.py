import hpprime as h
import MENU as m
import ohmslaw as ohmslaw
import combinations as combo
import PowerEnergy as WJ
import DCSimplify as DCS

def DC_Main():
    while True: 
        # Show button-based menu
        choice = m.create_button_menu("ΩLaw", "Combos", "Simplify","W or J"," ")

        if choice == 0:
            ohmslaw.ohmslaw_main()
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
        elif choice == 3:
            m.screenClear()
            h.eval('print("Not implemented yet.")')
            h.eval('wait(2)')
            m.screenClear()
        elif choice == 4 or choice == 5 or choice == 6:  # Exit
            m.screenClear()
            h.eval('print("Goodbye!")')
            break
        else:
            # Soft key press that wasn't mapped
            m.screenClear()
            h.eval('print("Invalid selection.")')
            h.eval('wait(2)')
            m.screenClear()