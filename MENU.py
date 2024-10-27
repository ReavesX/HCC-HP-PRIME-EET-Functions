from math import log10, pi, sqrt # Commonly used.
import cmath as c
import hpprime as h
import math as m


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    H P   P r i m e   I / O   R o u t i n e s -- Authored by Mike Markowski, mike.ab3ap@gmail.com
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def eng(x, sigfigs=0):
  """Return x in engineering notation.  That is, mantissa and exponent
  where mantissa is between -999 and 999, and exponent a multiple of
  3.  If exponent is in [-12,12] then SI prefix is used.
  """

  if x == 0:
    return '0'

  siPrefix={-12:'p',-9:'n',-6:'µ',-3:'m',0:'',3:'k',6:'M',9:'G',12:'T'}

  # Convert x to mantissa and exponent.
  exp = int(m.floor(log10(abs(x)))) # floor() needed for exp<0.
  mant = x/10**exp
  # Round mantissa to requested number of significant figures.
  mant = round(mant, sigfigs-1) if sigfigs > 0 else mant
  # Adjust so that exponent is multiple of 3.
  mult3 = exp % 3   # How many mulitples-of-three exponent must be decreased.
  exp -= mult3    # Decrease exponent.
  mant *= 10**mult3 # Increase mantissa.
  # Create format to pretty print.
  lenMant = len(str(int(abs(mant)))) # Number of digits left of decimal pt.
  fmt = '%%.%df' % max(0, sigfigs-lenMant)
  # Convert exponent to SI prefix.
  sExp = 'e%d ' % exp if abs(exp) > 12 else ' '+siPrefix[exp]
  return (fmt % mant) + sExp

def mouseClear():
  while h.eval('mouse(1)')>=0:
    pass # Clear event queue.

def mousePt():
  while True:
    h.eval('wait(0.1)')     # Throttle i/o loop.
    f1,f2 = h.eval('mouse') # Touch info for fingers 1 and 2.
    if len(f1) > 0:         # Got a finger touch!
      return f1             # [x,y,xOrig,yOrig,type], [x,y,xOrig,yOrig,type].

def screenClear():
  h.eval('print')  # Clear terminal.
  h.eval('rect()') # Clear graphics.

def softPick(pt):         # pt is [x, y, xOrig, yOrig, type]
  return -1 if pt[1]<220 else pt[0]//53 # Soft button is 53x20 pixels.

def toAVars(varName, val):
    cmd = 'AVars("%s"):=CAS.eval("%.11e")' % (varName, val) # 12 sig figs.
    h.eval(cmd)
  
  
  
# App begin
def welcomeScreen():
  h.eval('print') # Clear terminal.
  h.eval('print("\n\n                           HCC EET/CET Library                     \n\n")')
  h.eval('print("Version: 3.0.4 Sept 2024\n\n")')
  h.eval('print("Bugs & suggestions to:")')
  h.eval('print("Donald Jackson, donjacks0n@proton.me")')
  h.eval('wait(3)')
  screenClear()
  
def mainMenuChoices():
  while True:
    h.eval('print("Select an option below:")')
    mouseClear() # Ignore prior key bounces.
    h.eval('wait(0.1)') # Throttle i/o loop.
    h.eval('drawmenu("OhmsLaw", "Transistors", "ICs", "", "Exit")') # Main menu.
    m = mousePt()
    b = softPick(m)
    if b == 0:
      ohmsLaw()
    elif b == 1:
      pass
    elif b == 5:
      h.eval('print') # Clear terminal.
      print('\n%18s*~- Goodbye -~*' % ' ') # Clear terminal.
      h.eval('wait(0.5)')
      h.eval('print')
      break

def voltageMenu():
        screenClear()
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
                screenClear()
                return

            if U == 1:   Current_Amps = 1e-6*T     # uA
            elif U == 2: Current_Amps = 1e-3*T # mA
            else:        Current_Amps = T # A
            
            
            if V == 1:   RZ_Ohms = B     # m
            elif V == 2: RZ_Ohms = 1e3*B # 
            else: RZ_Ohms = 1e6*B
                
            voltage = RZ_Ohms*Current_Amps # Calculate Voltage
            
            toAVars('Voltage', voltage)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(voltage,3),x,y))
                
        if c==2: # Voltage by Power and Current
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"uA","mA","A"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Watt","GW","MW"},{63,15,1}}},\
            "Voltage", {"Current:","","Power:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
                
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Current_Amps = 1e-6*T     # uA
            elif U == 2: Current_Amps = 1e-3*T # mA
            else:        Current_Amps = T # A
                
                
            if V == 1:   Power_Watts = B     # m
            elif V == 2: Power_Watts = 1e3*B # 
            else: Power_Watts = 1e6*B
                    
            voltage = Power_Watts/Current_Amps # Calculate Voltage
                
            toAVars('Voltage', voltage)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(voltage,3),x,y))
            
        if c==3: # Voltage by Resistance and Power
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"W","GW","MW"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Ohm","Kilo-Ohm","Mega-Ohm"},{63,15,1}}},\
            "Voltage", {"Current:","","Resistance/Impedence:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Power_Watts = T     # m
            elif U == 2: Power_Watts = 1e3*T # 
            else: Power_Watts = 1e6*T
            
            
            if V == 1:   RZ_Ohms = B     # m
            elif V == 2: RZ_Ohms = 1e3*B # 
            else: RZ_Ohms = 1e6*B
                
            voltage = sqrt(RZ_Ohms*Power_Watts) # Calculate Voltage
                
            toAVars('Voltage', voltage)
            x,y = 123,120 # Coordinates to place result at
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(voltage,3),x,y))
            
        if c == 4: # Return to ohms law
            screenClear()
            ohmsLaw()
             
def currentMenu():
        screenClear()
        c = h.eval('X:=0;choose(X,"Current","V/R" , "W/E" , "SQRT(W/R)","Cancel")')
        s = '' # Result to be printed when calculated.
        if c==1: # Current by Voltage and Resistance
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Ohm","Kilo-Ohm","Mega-Ohm"},{63,15,1}}},\
            "Voltage", {"Voltage:","","Resistance/Impedence:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V
            
            
            if V == 1:   RZ_Ohms = B     # ohms
            elif V == 2: RZ_Ohms = 1e3*B # K-ohms 
            else: RZ_Ohms = 1e6*B        # M-ohms
                
            current = Voltage_volts/RZ_Ohms # Calculate Voltage
            
            toAVars('Voltage', current)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(current,3),x,y))
                
        if c==2: # Current by Power and Voltage
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Watt","GW","MW"},{63,15,1}}},\
            "Current", {"Voltage:","","Power:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
                
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V

                
                
            if V == 1:   Power_Watts = B     # m
            elif V == 2: Power_Watts = 1e3*B # 
            else: Power_Watts = 1e6*B
                    
            current = Power_Watts/Voltage_volts # Calculate Voltage
                
            toAVars('Voltage', current)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(current,3),x,y))
            
        if c==3: # Current by Resistance and Power
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"W","GW","MW"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Ohm","Kilo-Ohm","Mega-Ohm"},{63,15,1}}},\
            "Current ", {"Power:","","Resistance/Impedence:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Power_Watts = T     # m
            elif U == 2: Power_Watts = 1e3*T # 
            else: Power_Watts = 1e6*T
            
            
            if V == 1:   RZ_Ohms = B     # m
            elif V == 2: RZ_Ohms = 1e3*B # 
            else: RZ_Ohms = 1e6*B
                
            current = sqrt(Power_Watts/RZ_Ohms) # Calculate Voltage
                
            toAVars('Voltage', current)
            x,y = 123,120 # Coordinates to place result at
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(current,3),x,y))
            
        if c == 4: # Return to ohms law
            screenClear()
            ohmsLaw()

def resistanceMenu():
        screenClear()
        c = h.eval('X:=0;choose(X,"Resistance","V/I" , "(V^2)/W" , "W/(I^2)","Cancel")')
        s = '' # Result to be printed when calculated.
        if c==1: # Resistance by Voltage and Current 
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,0}},\
            {V,{"uA","mA","A"},     {63,15,0}},\
            "Resistance", {"Voltage:","","Current :",""},\
            {"","","",""},\
            {000,0,0,0},{000,00,0,0}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V
            
            
            if V == 1:   Current_Amps = 1e-6*B     # uA
            elif V == 2: Current_Amps = 1e-3*B # mA
            else: Current_Amps = B        # amps
                
            resistance = Voltage_volts/Current_Amps # Calculate resistance
            
            toAVars('Voltage', resistance)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(resistance,3),x,y))
                
        if c==2: # resistance by Power and Voltage
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,1}},\
            {V,{"Watt","GW","MW"},{63,15,1}}},\
            "Resistance", {"Voltage:","","Power:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
                
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V

                
                
            if V == 1:   Power_Watts = B     # m
            elif V == 2: Power_Watts = 1e3*B # 
            else: Power_Watts = 1e6*B
                    
            resistance = Voltage_volts**2 / Power_Watts # Calculate Voltage
                
            toAVars('Voltage', resistance)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(resistance,3),x,y))
            
        if c==3: # Resistance by Current  and Power
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"W","GW","MW"},     {63,15,0}},\
            {B,[0],               {40,20,0}},\
            {V,{"uA","mA","A"},     {63,15,0}},\
            "Resistance", {"Power:","","Current:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Power_Watts = T     # m
            elif U == 2: Power_Watts = 1e3*T # 
            else: Power_Watts = 1e6*T
            
            
            if V == 1:   Current_Amps = 1e-6*B     # m
            elif V == 2: Current_Amps = 1e-3*B # 
            else: Current_Amps = B
                
            resistance = Power_Watts/(Current_Amps**2) # Calculate Voltage
                
            toAVars('Voltage', resistance)
            x,y = 123,120 # Coordinates to place result at
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(resistance,3),x,y))
            
        if c == 4: # Return to ohms law
            screenClear()
            ohmsLaw()


def powerMenu():
        screenClear()
        c = h.eval('X:=0;choose(X,"Power","V*I" , "R*I^2" , "V^2/R","Cancel")')
        s = '' # Result to be printed when calculated.
        if c==1: # Power by Voltage and Current 
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,0}},\
            {V,{"uA","mA","A"},     {63,15,0}},\
            "Power", {"Voltage:","","Current :",""},\
            {"","","",""},\
            {000,0,0,0},{000,00,0,0}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V
            
            
            if V == 1:   Current_Amps = 1e-6*B     # uA
            elif V == 2: Current_Amps = 1e-3*B # mA
            else: Current_Amps = B        # amps
                
            power = Voltage_volts*Current_Amps # Calculate resistance
            
            toAVars('Voltage', power)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(power,3),x,y))
                
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
                screenClear()
                return

            if U == 1:   resistance_ohms = T     # mV
            elif U == 2: resistance_ohms = 1e3*T # V
            else: resistance_ohms = 1e6*T

                
                
            if V == 1:   Current_Amps = 1e-6*B     # m
            elif V == 2: Current_Amps = 1e-3*B # 
            else: Current_Amps = B
                    
            power = resistance_ohms * (Current_Amps**2) # Calculate Voltage
                
            toAVars('Voltage', power)
            x,y = 123,120
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(power,3),x,y))
            
        if c==3: # Resistance by Current  and Power
            
            T,U,B,V,res = h.eval('res:=input(\
            {{T,[0],               {40,20,0}},\
            {U,{"mV","V"},     {63,15,0}},\
            {B,[0],               {40,20,0}},\
            {V,{"Ohms","Kilo-Ohms","MegaOhms"},     {63,15,0}},\
            "Resistance", {"Power:","","Current:",""},\
            {"","","",""},\
            {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}')
            
            if res == 0: # User hit CANCEL.
                screenClear()
                return

            if U == 1:   Voltage_volts = 1e-3*T     # mV
            elif U == 2: Voltage_volts = T # V
            
            
            if V == 1:   resistance_ohms = T     # mV
            elif V == 2: resistance_ohms = 1e3*T # V
            else: resistance_ohms = 1e6*T
                
            power = (Voltage_volts**2)/(resistance_ohms) # Calculate Voltage
                
            toAVars('Voltage', power)
            x,y = 123,120 # Coordinates to place result at
            h.eval('textout_p("V = %sV", %d,%d)' % (eng(power,3),x,y))
            
        if c == 4: # Return to ohms law
            screenClear()
            ohmsLaw()




def ohmsLaw():
  screenClear()
  h.eval('print("Select an option below:")')
  while True:
    mouseClear() # Ignore prior key bounces.
    h.eval('wait(0.1)') # Throttle i/o loop.
    h.eval('drawmenu("Voltage", "Current", "R or Z", "Power"," ", "Back")') # Main menu.
    m = mousePt()
    b = softPick(m)
    if b == 0:
      voltageMenu()
      
    elif b == 1:
      currentMenu()
  
    elif b == 2:
        resistanceMenu()
    
    elif b == 3:
        powerMenu()
    
    elif b == 4:
        pass
    
    elif b == 5:
      screenClear()
      mainMenuChoices()

def main():
  welcomeScreen()
  mainMenuChoices()


main()
