# HP‑Prime EE‑CpE Applet

*Version 2.1.2*

This HP Prime calculator applet is designed specifically for students in the Computer Engineering and Electronics Engineering Technology (CpE/EE) program at Hillsborough Community College. It provides quick access to commonly used engineering formulas, conversions, and calculation tools — all from the calculator itself.

> ⚠️ **Note:** This app **only runs on the HP Prime graphing calculator** and is not designed to run in a standard desktop Python environment.

---

## 📦 Table of Contents

1. [Features](#features)  
2. [Installation](#installation)  
3. [Usage](#usage)  
4. [Modules](#modules)  
5. [Examples](#examples)  
6. [Planned Features](#planned-features)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## ✅ Features

- Menu-driven user interface for solving EE/CpE problems
- Works **offline**, directly on the HP Prime calculator
- Modular structure (`main.py`, `MENU.py`)
- Simple to expand with new formulas and conversion utilities
- Tested using representative calculations

---

## 📥 Installation

### Requirements

- HP Prime calculator (physical or emulator)
- HP Prime Connectivity Kit

### Steps

1. Clone or download this repository:

   ```bash
   git clone https://github.com/ReavesX/HpPrime-EE-CpE-Applet.git
   ```

2. Open the **HP Prime Connectivity Kit** on your PC.

3. Connect your HP Prime calculator via USB.

4. Drag and drop files into the calculator’s python program, or create a copy and name it accordingly.

5. On your calculator, run the python app to start the applet.

---

## ▶️ Usage

After launching the program on the calculator:

```
HP‑Prime EE/CpE Toolbox:
1 – Resistor Networks
2 – Capacitor Charge/Discharge
3 – Circuit Conversions (e.g., Y-Δ)
4 – [More coming soon!]
```

Use the number keys or arrow keys to choose an operation. You'll be prompted to enter relevant values, and the applet will output the result directly.

---

## 📂 Modules

### `main.py`
- Main entry point
- Displays the menu and routes to functions

### `MENU.py`
- User interaction handler
- Manages prompt, input, and formatting

### `Tests/`
- Contains test scripts used for PC-side validation
- Uses standard unit-testing ideas, but only for logic mirroring the calculator’s functions

> ❗ These tests **do not run on the HP Prime** but help during development.

---

## 💡 Examples

### Example 1: Parallel Resistors

```
R1 = 220 Ω, R2 = 330 Ω, R3 = 470 Ω  
Output: R_eq ≈ 96.3 Ω
```

### Example 2: Capacitor Discharge

```
C = 10 µF, R = 1 kΩ, V₀ = 5 V, t = 5 ms  
Output: V(t) ≈ 1.84 V
```

---

## 🚧 Planned Features

Future features under development include:

- Inductor time constants (RL/LC circuits)
- Phasor transformation and impedance calculations
- Transistor region solver
- Digital logic calculators (e.g., K-map simplifier)
- Polyphase system analysis
- Delta-Wye and Wye-Delta conversions (multi-node)
- Op-amp solver with gain & feedback

---

## 🤝 Contributing

Contributions welcome!

### To contribute:

1. Fork this repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-new-feature
   ```
3. Add your new `.py` file and update `main.py` or `MENU.py`
4. Submit a pull request with a description of your addition

**Please** add tests in the `Tests/` folder if possible to validate your logic during development.

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

Special thanks to the faculty and students at Hillsborough Community College for providing curriculum feedback and testing the app in real coursework settings.

---

> 🎓 *Built by students, for students — this app is your digital lab partner for EE/CpE success on the HP Prime.*
