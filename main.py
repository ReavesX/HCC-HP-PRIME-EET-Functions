import MENU as m
import hpprime as h
import CALS as CALS

#import modules

def main():
    m.welcomeScreen()

    while True: 
        # Show button-based menu
        choice = m.create_button_menu("CALS", " x ", " x ", " x ", " x ")

        if choice == 0:
            CALS.cals_main()
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
        elif choice == 4:
            m.screenClear()
            h.eval('print("Not implemented yet.")')
            h.eval('wait(2)')
            m.screenClear()
        elif choice == 5:
            m.screenClear()
            h.eval('print("Not implemented yet.")')
            h.eval('wait(2)')
            m.screenClear()
        elif choice == 6:  # Exit
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