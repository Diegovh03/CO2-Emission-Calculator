import tkinter as tk
from tkinter import messagebox

class CO2CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("CO2 Emissions Calculator")

        # Define emission factors (gCO2eq/kWh) as an instance variable
        self.emission_factors = {'Hydro': 4, 'Natural Gas': 469, 'Wind': 11, 'Solar': 41, 'Coal': 1001}

        # Create input fields for energy consumption
        self.entries = {}
        row = 0
        for source, factor in self.emission_factors.items():
            tk.Label(root, text=f"{source} (kWh):").grid(row=row, column=0, sticky="e")
            entry = tk.Entry(root)
            entry.grid(row=row, column=1)
            self.entries[source] = entry
            row += 1
        
        # Calculate button
        self.calculate_btn = tk.Button(root, text="Calculate", command=self.calculate_emissions)
        self.calculate_btn.grid(row=row, columnspan=2)
        
        # Result display
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_var)
        self.result_label.grid(row=row+1, columnspan=2)

    def calculate_emissions(self):
        total_emissions = 0
        for source, entry in self.entries.items():
            try:
                consumption = float(entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for {source}. Please enter a number.")
                return
            factor = self.emission_factors[source]
            emissions = consumption * factor
            total_emissions += emissions
        
        self.result_var.set(f"Total CO2 emissions: {total_emissions} gCO2eq")

if __name__ == "__main__":
    root = tk.Tk()
    app = CO2CalculatorApp(root)
    root.mainloop()