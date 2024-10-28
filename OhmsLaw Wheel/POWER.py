import MENU as menu
import hpprime as h
from math import sqrt
import ohmsLaw as OL

def powerMenu():
        menu.screenClear()
        c = h.eval('X:=0;choose(X,"Power","V*I" , "R*I^2" , "V^2/R","Cancel")')
        s = '' # Result to be printed when calculated.
        if c==1: # Power by Voltage and Current 
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"uA","mA","A"},{63,15,1}}},\
            "Power", {"Voltage:","","Current:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V
            
            
            if V == 1:   Current_Amps = 1e-6*B     # uA
            elif V == 2: Current_Amps = 1e-3*B # mA
            else: Current_Amps = B        # amps
                
            power = Voltage_volts*Current_Amps # Calculate resistance
            
            menu.toAVars('Voltage', power)
            x,y = 123,120
            h.eval('textout_p("P = %sW", %d,%d)' % (menu.eng(power,3),x,y))
                
        if c==2: # Power by Resistance and Current
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"Ohms","Kilo-Ohms","MegaOhms"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"uA","mA","A"},{63,15,1}}},\
            "Power", {"Resistance:","","Current:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
                
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   resistance_ohms = T     # mV
            elif U == 2: resistance_ohms = 1e3*T # V
            else: resistance_ohms = 1e6*T

                
                
            if V == 1:   Current_Amps = 1e-6*B     # m
            elif V == 2: Current_Amps = 1e-3*B # 
            else: Current_Amps = B
                    
            power = resistance_ohms * (Current_Amps**2) # Calculate Voltage
                
            menu.toAVars('Voltage', power)
            x,y = 123,120
            h.eval('textout_p("P = %sW", %d,%d)' % (menu.eng(power,3),x,y))
            
        if c==3: # Resistance by Current  and Power
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Ohms","kΩ","MΩ"},{63,15,1}}},\
            "Power", {"Voltage:","","Resistance:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V
            
            
            if V == 1:   resistance_ohms = T     # mV
            elif V == 2: resistance_ohms = 1e3*T # V
            else: resistance_ohms = 1e6*T
                
            power = (Voltage_volts**2)/(resistance_ohms) # Calculate Voltage
                
            menu.toAVars('Voltage', power)
            x,y = 123,120 # Coordinates to place result at
            h.eval('textout_p("P = %sW", %d,%d)' % (menu.eng(power,3),x,y))
            
        if c == 4: # Return to main
        
            menu.screenClear()
            menu.mainMenuChoices()