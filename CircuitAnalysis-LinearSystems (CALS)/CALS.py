import hpprime as h
import menu as m
import DC as DC

def cals_main():
    while True: 
        # Show button-based menu
        choice = m.create_button_menu("DC Fund", " x ", " x ", " x ", " x ")

        if choice == 0:
            DC.DC_main()
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
        elif choice == 4:  # Exit
            m.screenClear()
            h.eval('print("Not implemented yet.")')
        elif choice == 5:  # Exit
            m.screenClear()
            h.eval('print("Not implemented yet.")')
        elif choice == 6:  # Exit
            m.screenClear()
            h.eval('print("Goodbye!")')
            break
        else:
            # Soft key press that wasn't mapped
            m.screenClear()
            h.eval('print("Invalid selection.")')
            h.eval('wait(2)')
