from math import log10, pi, sqrt # Commonly used.
import cmath as c
import hpprime as h
import math as m
import ohmsLaw as OL
import RESISTANCE as r
import VOLTAGE as v
import POWER as p

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
      OL.ohmsLaw()
    elif b == 1:
      pass
    elif b == 5:
      h.eval('print') # Clear terminal.
      print('\n%18s*~- Goodbye -~*' % ' ') # Clear terminal.
      h.eval('wait(0.5)')
      h.eval('print')
      break

def main():
  welcomeScreen()
  mainMenuChoices()


main()
