import MENU as menu
import hpprime as h
from math import sqrt

def resistanceMenu():
        menu.screenClear()
        c = h.eval('X:=0;choose(X,"Resistance","V/I" , "(V^2)/W" , "W/(I^2)","Cancel")')
        s = '' # Result to be printed when calculated.
        if c==1: # Resistance by Voltage and Current 
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"uA","mA","A"},{63,15,1}}},\
            "Resistance", {"Voltage:","","Current:",""},\
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
                
            resistance = Voltage_volts/Current_Amps # Calculate resistance
            
            menu.toAVars('Voltage', resistance)
            x,y = 123,120
            h.eval('textout_p("R = %sΩ", %d,%d)' % (menu.eng(resistance,3),x,y))
                
        if c==2: # resistance by Power and Voltage
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Watt","kW","MW"},{63,15,1}}},\
            "Resistance", {"Voltage:","","Power:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
                
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V

                
                
            if V == 1:   Power_Watts = B     # m
            elif V == 2: Power_Watts = 1e3*B # 
            else: Power_Watts = 1e6*B
                    
            resistance = Voltage_volts**2 / Power_Watts # Calculate Voltage
                
            menu.toAVars('Voltage', resistance)
            x,y = 123,120
            h.eval('textout_p("R = %sΩ", %d,%d)' % (menu.eng(resistance,3),x,y))
            
        if c==3: # Resistance by Current  and Power
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"W","kW","MW"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"uA","mA","A"},{63,15,1}}},\
            "Resistance", {"Power:","","Current:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   Power_Watts = T     # m
            elif U == 2: Power_Watts = 1e3*T # 
            else: Power_Watts = 1e6*T
            
            
            if V == 1:   Current_Amps = 1e-6*B     # m
            elif V == 2: Current_Amps = 1e-3*B # 
            else: Current_Amps = B
                
            resistance = Power_Watts/(Current_Amps**2) # Calculate Voltage
                
            menu.toAVars('Voltage', resistance)
            x,y = 123,120 # Coordinates to place result at
            h.eval('textout_p("V = %sΩ", %d,%d)' % (menu.eng(resistance,3),x,y))
            
        if c == 4: # Return to ohms law
            menu.screenClear()
            menu.mainMenuChoices()