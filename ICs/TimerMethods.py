from typing import Optional

# Base class for Characteristics
class Tmr_Characteristics:
    def __init__(self, voltage: Optional[float] = None, power: Optional[float] = None, resistance: Optional[float] = None, current: Optional[float] = None, capacitance: Optional[float] = None, frequency: Optional[float] = None, high_time: Optional[float] = None, low_time: Optional[float] = None, period: Optional[float] = None):
        self.resistance: Optional[float] = resistance
        self.capacitance: Optional[float] = capacitance
        self.frequency: Optional[float] = frequency
        self.high_time: Optional[float] = high_time
        self.low_time: Optional[float] = low_time
        self.period: Optional[float] = period

    def return_val(self) -> None:
        if self.capacitance is not None:
            print(f'Capacitance: {self.capacitance} Farads')
        if self.frequency is not None:
            print(f'Frequency: {self.frequency} Hz')
        if self.high_time is not None:
            print(f'High Time: {self.high_time} seconds')
        if self.low_time is not None:
            print(f'Low Time: {self.low_time} seconds')
        if self.period is not None:
            print(f'Period: {self.period} seconds')
        if self.resistance is None and self.capacitance is None and self.frequency is None and self.high_time is None and self.low_time is None and self.period is None:
            print('Calculation not available.')

# Class for Astable 555 Timer Configuration
class Astable(Tmr_Characteristics):
    def __init__(self, r1: Optional[float] = None, r2: Optional[float] = None, c1: Optional[float] = None):
        super().__init__()
        self.r1: Optional[float] = r1
        self.r2: Optional[float] = r2
        self.c1: Optional[float] = c1

    def calculate_high_low_times(self) -> None:
        if self.r1 is not None and self.r2 is not None and self.c1 is not None:
            self.high_time = 0.693 * (self.r1 + self.r2) * self.c1
            self.low_time = 0.693 * self.r2 * self.c1
            self.return_val()
        else:
            raise ValueError("Missing values for R1, R2, or C1.")

    def calculate_resistances(self) -> None:
        if self.high_time is not None and self.low_time is not None and self.c1 is not None:
            self.r2 = self.low_time / (0.693 * self.c1)
            self.r1 = (self.high_time / (0.693 * self.c1)) - self.r2
            self.return_val()
        else:
            raise ValueError("Missing values for High Time, Low Time, or C1.")

    def calculate_frequency(self) -> None:
        if self.r1 is not None and self.r2 is not None and self.c1 is not None:
            self.frequency = 1.44 / ((self.r1 + (2 * self.r2)) * self.c1)
            self.return_val()
        else:
            raise ValueError("Missing values for R1, R2, or C1.")

    def calculate_capacitance(self) -> None:
        if self.low_time is not None and self.r2 is not None:
            self.capacitance = self.low_time / (0.693 * self.r2)
            self.return_val()
        else:
            raise ValueError("Missing values for Low Time or R2.")

# Class for Monostable 555 Timer Configuration
class Monostable(Tmr_Characteristics):
    def __init__(self, r1: Optional[float] = None, c1: Optional[float] = None):
        super().__init__()
        self.r1: Optional[float] = r1
        self.c1: Optional[float] = c1

    def calculate_period(self) -> None:
        if self.r1 is not None and self.c1 is not None:
            self.period = 1.1 * self.r1 * self.c1
            self.return_val()
        else:
            raise ValueError("Missing values for R1 or C1.")

    def calculate_resistance(self) -> None:
        if self.period is not None and self.c1 is not None:
            self.r1 = self.period / (1.1 * self.c1)
            self.return_val()
        else:
            raise ValueError("Missing values for Period or C1.")

    def calculate_capacitance(self) -> None:
        if self.period is not None and self.r1 is not None:
            self.capacitance = self.period / (1.1 * self.r1)
            self.return_val()
        else:
            raise ValueError("Missing values for Period or R1.")