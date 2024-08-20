import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def rocket_equation(ve, m0, mf):
    return ve * np.log(m0 / mf)

def generate_data():
    try:
        # Retrieve user inputs
        ve = float(entry_ve.get())
        m0 = float(entry_m0.get())
        mf = float(entry_mf.get())

        # Generate data for mass ratio and delta_v
        mass_ratio = np.linspace(mf, m0, 100)
        delta_v = rocket_equation(ve, m0, mass_ratio)

        # Create a DataFrame
        data = {
            'Initial Mass (kg)': [m0] * 100,
            'Final Mass (kg)': mass_ratio,
            'Change in Velocity (m/s)': delta_v
        }
        df = pd.DataFrame(data)

        # Ask user where to save the Excel file
        save_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            title="Save the Excel file"
        )

        if save_path:
            df.to_excel(save_path, index=False)
            messagebox.showinfo("Success", f"Data saved to {save_path}")

            # Plot the velocity curve
            plt.plot(mass_ratio, delta_v)
            plt.xlabel('Final Mass (kg)')
            plt.ylabel('Change in Velocity (m/s)')
            plt.title('Rocket Velocity Curve')
            plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = Tk()
root.title("Rocket Equation Simulation")

# Labels and entry fields for user input
Label(root, text="Exhaust Velocity (m/s):").grid(row=0, column=0, padx=10, pady=5)
entry_ve = Entry(root)
entry_ve.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Initial Mass (kg):").grid(row=1, column=0, padx=10, pady=5)
entry_m0 = Entry(root)
entry_m0.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Final Mass (kg):").grid(row=2, column=0, padx=10, pady=5)
entry_mf = Entry(root)
entry_mf.grid(row=2, column=1, padx=10, pady=5)

# Button to generate the data and save the Excel file
Button(root, text="Generate Data", command=generate_data).grid(row=3, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
