# HCC Circuit Analysis Tool

## Author
Donald Jackson

## Date
05/23/2024

## Description
This project contains a set of tools for circuit analysis, including calculations for resistance, impedance, Ohm's Law, and more. The scripts are designed to run on Python, but they can also be adapted for use on an HP PRIME G2 Calculator.

## Features
- **Ohm's Law Calculations**
- **Resistance Calculations**
- **JWL/JWC Calculations**
- **BJT Calculations**
- **555 Timer Calculations**

## Installation Instructions

### Running on a Computer
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/ReavesX/HCC-HP-PRIME-EET-Functions/.git
   cd circuit-analysis-tool
2. Ensure you have Python installed:
   Download and install Python from python.org.
3. Run the Script:
   in shell/terminal: 
   python main.py 

### Setting Up as a New App on HP PRIME G2 Calculator
1. **Download HP Prime Connectivity Kit:**
   Download and install the HP Prime Connectivity Kit from the [HP official website](https://www.hp.com/us-en/shop/pdp/hp-prime-graphing-calculator).

2. **Connect Your Calculator:**
   Connect your HP PRIME G2 Calculator to your computer using a USB cable.

3. **Transfer the Scripts:**
   - Open the HP Prime Connectivity Kit.
   - Drag and drop the Python scripts (`main.py`, `jwl.py`, `tmr_555.py`, `OhmsLaw.py`, `Resistance.py`, `BJTs.py`) into the `Programs` section of the Connectivity Kit.

4. **Create a New App:**
   - On your HP PRIME G2 Calculator, press the `Apps` key.
   - Select `+ New` to create a new app.
   - Name the new app (e.g., `CircuitAnalysis`).

5. **Set Up the Python App:**
   - Press the `Shift` key and then the `1` key to open the `Program` editor.
   - In the new program editor, input the following Python code to integrate the scripts:

     ```python
     # Circuit Analysis Tool

     import jwl as jwl
     import tmr_555 as tmr
     import OhmsLaw as OL
     import Resistance as RZ
     import BJTs as bjt

     def main():
         option = int(input('''1 for Ohms Law, 2 for Resistance,
     3 for JWL/JWC, 4 for Bjts,
     5 for 555timer: '''))
             
         if option == 1:
             OL.calculate_ohms_law()  # Replace with the actual function name
         elif option == 2:
             RZ.calculate_resistance()  # Replace with the actual function name
         elif option == 3: 
             jwl.calculate_jwl()  # Replace with the actual function name
         elif option == 4:
             bjt.calculate_bjt()  # Replace with the actual function name
         elif option == 5: 
             tmr.calculate_timer()  # Replace with the actual function name
         else:
             print("Invalid option")

     if __name__ == "__main__":
         main()
     ```

   - Ensure each of the imported modules (`jwl.py`, `tmr_555.py`, `OhmsLaw.py`, `Resistance.py`, `BJTs.py`) are included in your calculator's memory.

6. **Save and Run the App:**
   - Save the new program.
   - Exit the program editor and return to the home screen.
   - Select the `CircuitAnalysis` app from the app list.
   - Press `Enter` to run the app.

## Usage
1. **Select an Option:**
   When prompted, enter the corresponding number to perform a specific calculation:
   - `1` for Ohm's Law Calculations
   - `2` for Resistance Calculations
   - `3` for JWL/JWC Calculations
   - `4` for BJT Calculations
   - `5` for 555 Timer Calculations

2. **Follow On-Screen Instructions:**
   Enter the required values as prompted by the program.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.