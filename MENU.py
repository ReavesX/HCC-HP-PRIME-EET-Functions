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
    



  '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    HCC  P r i m e    -- Authored by Donald Jackson, donjacks0n@proton.me
  
  '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# App begin
def welcomeScreen():
  h.eval('print') # Clear terminal.
  h.eval('print("\n\n                           HCC EET/CET Library                     \n\n")')
  h.eval('print("Version: 3.0.4 Sept 2024\n\n")')
  h.eval('print("Bugs & suggestions to:")')
  h.eval('print("Donald Jackson, donjacks0n@proton.me")')
  h.eval('wait(3)')
  screenClear()

def display_and_store_result(label, value, x=123, y=120, sigfigs=3):
    """

    Args:
        label (str): Name to save the variable as in AVars (e.g., "Voltage")
        value (float): The computed result
        x (int): X-coordinate for on-screen output
        y (int): Y-coordinate for on-screen output
        sigfigs (int): Significant figures for engineering notation

    """
    toAVars(label, value)
    formatted = eng(value, sigfigs)

    # Fixed output function, arraying in the previous one did not work as intended unforutnately.
    h.eval('textout_p("%s: %s", %d, %d)' % (label, formatted, x, y))

    h.eval('wait(3)') # Wait for 3 seconds to see the output

def create_button_menu(choice1, choice2, choice3, choice4, choice5):
  """
  Creates a standardized input dialog for electrical calculations.
    
  Args:
      choice1: First Menu Choice
      choice2: Second Menu Choicen
      choice3: Third Menu Choice
      choice4: Fourth Menu Choice
      choice5: Fifth Menu Choice
        
    Returns:
        Tuple containing the user inputs or None if cancelled
  """
  
    
  screenClear()
  h.eval('print("Select an option below:")')
  while True:
    mouseClear() # Ignore prior key bounces.
    h.eval('wait(0.1)') # Throttle i/o loop.
    h.eval('drawmenu("%s", "%s", "%s", "%s","%s", "Back")' % (
                          choice1, choice2, choice3, choice4, choice5)) # Main menu.
    m = mousePt()
    b = softPick(m)
    return b
  
def create_dropdown_menu(Title, choice1, choice2, choice3, choice4, choice5):
    """
    Displays a standardized dropdown menu with five selectable options using HP Prime's choose().

    Args:
        Title: The title of the dropdown menu (string)
        choice1: Label for the first option (string)
        choice2: Label for the second option (string)
        choice3: Label for the third option (string)
        choice4: Label for the fourth option (string)
        choice5: Label for the fifth option (string), typically used for "Cancel"

    Returns:
        Integer corresponding to the user's selected option:
            1 for choice1,
            2 for choice2,
            3 for choice3,
            4 for choice4,
            5 for choice5 (e.g., "Cancel")

        The function returns the selection index directly from HP Prime’s `choose()` function.
        Note: If the user cancels, they will still return the index of the "Cancel" entry (usually 5).
    """
    screenClear()
    expression = 'X:=0;choose(X,"' + Title + '","' + choice1 + '","' + choice2 + '","' + choice3 + '","' + choice4 + '","' + choice5 + '")'
    selection = h.eval(expression)
    return selection

def create_dialog(known_value_quantity, window_title, 
                 smallest_units1, mid_units1, largest_units1,
                 smallest_units2, mid_units2, largest_units2,
                 smallest_units3=None, mid_units3=None, largest_units3=None,
                 smallest_units4=None, mid_units4=None, largest_units4=None,
                 smallest_units5=None, mid_units5=None, largest_units5=None,
                 known_value1_label="", known_value2_label="", known_value3_label="",
                 known_value4_label="", known_value5_label=""):
    """
    Creates a standardized input dialog for electrical calculations.
    
    Args:
        known_value_quantity: Integer (2-5) indicating how many value/unit pairs to display
        window_title: String title for the dialog window
        smallest_units1, mid_units1, largest_units1: Unit labels for first quantity
        smallest_units2, mid_units2, largest_units2: Unit labels for second quantity
        smallest_units3, mid_units3, largest_units3: Optional unit labels for third quantity
        smallest_units4, mid_units4, largest_units4: Optional unit labels for fourth quantity
        smallest_units5, mid_units5, largest_units5: Optional unit labels for fifth quantity
        known_value1_label: Label for the first known value
        known_value2_label: Label for the second known value
        known_value3_label: Optional label for the third known value
        known_value4_label: Optional label for the fourth known value
        known_value5_label: Optional label for the fifth known value
        
    Returns:
        Tuple containing the user inputs or None if cancelled
    """
    if known_value_quantity == 2:
        T, U, B, V, res = h.eval('res:=input(\
        {{T,[0],               {40,20,0}},\
        {U,{"%s","%s","%s"},     {63,15,0}},\
        {B,[0],               {40,20,1}},\
        {V,{"%s","%s","%s"},{63,15,1}}},\
        "%s", {"%s","","%s",""},\
        {"","","",""},\
        {288,1,1,2},{288,1,1,2}); {T,U,B,V,res}' % (
            smallest_units1, mid_units1, largest_units1,
            smallest_units2, mid_units2, largest_units2,
            window_title, known_value1_label, known_value2_label
        ))
        
        if res == 0:  # User hit CANCEL
            screenClear()
            return None
        
        return T, U, B, V, res
        
    elif known_value_quantity == 3:
        F, U, D, V, T, W, res = h.eval('res:=input(\
        {{F,[0],               {40,20,0}},\
        {U,{"%s","%s","%s"},{63,15,0}},\
        {D,[0],               {40,20,1}},\
        {V,{"%s","%s","%s"},{63,15,1}},\
        {T,[0],               {40,20,2}},\
        {W,{"%s","%s","%s"},{63,15,2}}},\
        "%s",\
        {"%s","","%s","","%s",""},\
        {"","","","","",""},\
        {288,1,1,2},{288,1,1,2}); {F,U,D,V,T,W,res}' % (
            smallest_units1, mid_units1, largest_units1,
            smallest_units2, mid_units2, largest_units2,
            smallest_units3, mid_units3, largest_units3,
            window_title, known_value1_label, known_value2_label, known_value3_label
        ))
        
        if res == 0:  # User hit CANCEL
            screenClear()
            return None
        
        return F, U, D, V, T, W, res
        
    elif known_value_quantity == 4:
        F, U, D, V, T, W, G, X, res = h.eval('res:=input(\
        {{F,[0],               {40,20,0}},\
        {U,{"%s","%s","%s"},{63,15,0}},\
        {D,[0],               {40,20,1}},\
        {V,{"%s","%s","%s"},{63,15,1}},\
        {T,[0],               {40,20,2}},\
        {W,{"%s","%s","%s"},{63,15,2}},\
        {G,[0],               {40,20,3}},\
        {X,{"%s","%s","%s"},{63,15,3}}},\
        "%s",\
        {"%s","","%s","","%s","","%s",""},\
        {"","","","","","","",""},\
        {288,1,1,2},{288,1,1,2}); {F,U,D,V,T,W,G,X,res}' % (
            smallest_units1, mid_units1, largest_units1,
            smallest_units2, mid_units2, largest_units2,
            smallest_units3, mid_units3, largest_units3,
            smallest_units4, mid_units4, largest_units4,
            window_title, known_value1_label, known_value2_label, known_value3_label, known_value4_label
        ))
        
        if res == 0:  # User hit CANCEL
            screenClear()
            return None
        
        return F, U, D, V, T, W, G, X, res
        
    elif known_value_quantity == 5:
        F, U, D, V, T, W, G, X, H, Y, res = h.eval('res:=input(\
        {{F,[0],               {40,20,0}},\
        {U,{"%s","%s","%s"},{63,15,0}},\
        {D,[0],               {40,20,1}},\
        {V,{"%s","%s","%s"},{63,15,1}},\
        {T,[0],               {40,20,2}},\
        {W,{"%s","%s","%s"},{63,15,2}},\
        {G,[0],               {40,20,3}},\
        {X,{"%s","%s","%s"},{63,15,3}},\
        {H,[0],               {40,20,4}},\
        {Y,{"%s","%s","%s"},{63,15,4}}},\
        "%s",\
        {"%s","","%s","","%s","","%s","","%s",""},\
        {"","","","","","","","","",""},\
        {288,1,1,2},{288,1,1,2}); {F,U,D,V,T,W,G,X,H,Y,res}' % (
            smallest_units1, mid_units1, largest_units1,
            smallest_units2, mid_units2, largest_units2,
            smallest_units3, mid_units3, largest_units3,
            smallest_units4, mid_units4, largest_units4,
            smallest_units5, mid_units5, largest_units5,
            window_title, known_value1_label, known_value2_label, known_value3_label, known_value4_label, known_value5_label
        ))
        
        if res == 0:  # User hit CANCEL
            screenClear()
            return None
        
        return F, U, D, V, T, W, G, X, H, Y, res
    
    else:
        raise ValueError("known_value_quantity must be between 2 and 5")
