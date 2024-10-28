import MENU as menu
import hpprime as h
import math as m

def helpcurrentmenu():
    menu.screenClear()
    c = h.eval('X:=0;choose(X,"Current","V/R", "W/E", "SQRT(W/R)", "Cancel")')
    s = ''  # Result to be printed when calculated.

    if c == 1:  # Current by Voltage and Resistance
        T, U, B, V, res = h.eval('res:=input(\
            {{T,[0], {40,20,0}},\
            {U,{"mV","V"}, {63,15,0}},\
            {B,[0], {40,20,1}},\
            {V,{"Ohm","Kilo-Ohm","Mega-Ohm"},{63,15,1}}},\
            "Voltage", {"Voltage:","","Resistance/Impedance:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
        
        if res == 0:  # User hit CANCEL.
            menu.screenClear()
            return

        Voltage_volts = T * (1e-3 if U == 1 else 1)  # Convert mV to V if needed
        RZ_Ohms = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)  # Convert to Ohms

        current = Voltage_volts / RZ_Ohms  # Calculate Current
        menu.toAVars('Voltage', current)
        x, y = 123, 120
        h.eval('textout_p("I = %sA", %d, %d)' % (menu.eng(current, 3), x, y))

    elif c == 2:  # Current by Power and Voltage
        T, U, B, V, res = h.eval('res:=input(\
            {{T,[0], {40,20,0}},\
            {U,{"mV","V"}, {63,15,0}},\
            {B,[0], {40,20,1}},\
            {V,{"Watt","kW","MW"},{63,15,1}}},\
            "Current", {"Voltage:","","Power:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
        
        if res == 0:  # User hit CANCEL.
            menu.screenClear()
            return

        Voltage_volts = T * (1e-3 if U == 1 else 1)  # Convert mV to V if needed
        Power_Watts = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)  # Convert to Watts

        current = Power_Watts / Voltage_volts  # Calculate Current
        menu.toAVars('Voltage', current)
        x, y = 123, 120
        h.eval('textout_p("I = %sA", %d, %d)' % (menu.eng(current, 3), x, y))

    elif c == 3:  # Current by Resistance and Power
        T, U, B, V, res = h.eval('res:=input(\
            {{T,[0], {40,20,0}},\
            {U,{"W","kW","MW"}, {63,15,0}},\
            {B,[0], {40,20,1}},\
            {V,{"Ohm","Kilo-Ohm","Mega-Ohm"},{63,15,1}}},\
            "Current", {"Power:","","Resistance/Impedance:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
        
        if res == 0:  # User hit CANCEL.
            menu.screenClear()
            return

        Power_Watts = T * (1 if U == 1 else 1e3 if U == 2 else 1e6)  # Convert to Watts
        RZ_Ohms = B * (1 if V == 1 else 1e3 if V == 2 else 1e6)  # Convert to Ohms

        current = m.sqrt(Power_Watts / RZ_Ohms)  # Calculate Current
        menu.toAVars('Voltage', current)
        x, y = 123, 120  # Coordinates to place result at
        h.eval('textout_p("I = %sA", %d, %d)' % (menu.eng(current, 3), x, y))

    elif c == 4:  # Return to Ohm's law
            menu.screenClear()
            menu.mainMenuChoices()
