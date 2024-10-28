import MENU as menu
import hpprime as h
import POWER as p
import VOLTAGE as v
import RESISTANCE as r
import helpcurrent as hc

def ohmsLaw():
    menu.screenClear()
    h.eval('print("Select an option below:")')

    while True:
        menu.mouseClear()  # Ignore prior key bounces.
        h.eval('wait(0.1)')  # Throttle i/o loop.
        h.eval('drawmenu("Voltage", "Current", "R or Z", "Power"," ", "Back")')  # Main menu.
        m = menu.mousePt()
        b = menu.softPick(m)

        if b == 0:
            v.voltageMenu()
        elif b == 1:
            hc.helpcurrentmenu()
        elif b == 2:
            r.resistanceMenu()
        elif b == 3:
            p.powerMenu()
        elif b == 4:
            pass
        elif b == 5:
            menu.screenClear()
            menu.mainMenuChoices()
