import MENU as menu
import hpprime as h
from math import sqrt

def voltageMenu():
        menu.screenClear()
        c = h.eval('X:=0;choose(X,"Voltage","IR","W/I","SQRT(WR)","Cancel")')
        s = '' # Result to be printed when calculated.
        if c==1: # Voltage by Resistance and Current
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"uA","mA","A"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Ohm","Kilo-Ohm","Mega-Ohm"},{63,15,1}}},\
            "Voltage", {"Current:","","Resistance/Impedence:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   Current_Amps = 1e-6*T     # uA
            elif U == 2: Current_Amps = 1e-3*T # mA
            else:        Current_Amps = T # A
            
            
            if V == 1:   RZ_Ohms = B     # m
            elif V == 2: RZ_Ohms = 1e3*B # 
            else: RZ_Ohms = 1e6*B
                
            voltage = RZ_Ohms*Current_Amps # Calculate Voltage
            
            menu.toAVars('Voltage', voltage)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (menu.eng(voltage,3),x,y))
                
        if c==2: # Voltage by Power and Current
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"uA","mA","A"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Watt","kW","MW"},{63,15,1}}},\
            "Voltage", {"Current:","","Power:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
                
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   Current_Amps = 1e-6*T     # uA
            elif U == 2: Current_Amps = 1e-3*T # mA
            else:        Current_Amps = T # A
                
                
            if V == 1:   Power_Watts = B     # m
            elif V == 2: Power_Watts = 1e3*B # 
            else: Power_Watts = 1e6*B
                    
            voltage = Power_Watts/Current_Amps # Calculate Voltage
                
            menu.toAVars('Voltage', voltage)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (menu.eng(voltage,3),x,y))
            
        if c==3: # Voltage by Resistance and Power
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"W","kW","MW"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Ohm","Kilo-Ohm","Mega-Ohm"},{63,15,1}}},\
            "Voltage", {"Current:","","Resistance/Impedence:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                menu.screenClear()
                return

            if U == 1:   Power_Watts = T     # m
            elif U == 2: Power_Watts = 1e3*T # 
            else: Power_Watts = 1e6*T
            
            
            if V == 1:   RZ_Ohms = B     # m
            elif V == 2: RZ_Ohms = 1e3*B # 
            else: RZ_Ohms = 1e6*B
                
            voltage = sqrt(RZ_Ohms*Power_Watts) # Calculate Voltage
                
            menu.toAVars('Voltage', voltage)
            x,y = 123,120 # Coordinates to place result at
            h.eval('textout_p("V = %sV", %d,%d)' % (menu.eng(voltage,3),x,y))
            
        if c == 4: # Return to ohms law
            menu.screenClear()
            menu.mainMenuChoices()
