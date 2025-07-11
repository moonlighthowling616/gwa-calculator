import tkinter as tk
from tkinter import messagebox

class GradeCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GWA Calculator")
        self.root.geometry("420x220")

        tk.Label(root, text="Enter Student's Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.name = tk.Entry(root, width=30)
        self.name.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        tk.Label(root, text="Enter Grade Level & Section:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.trasec = tk.Entry(root, width=30)
        self.trasec.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        tk.Label(root, text="Enter Grades (comma-separated):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.grades = tk.Entry(root, width=30)
        self.grades.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.calculate = tk.Button(root, text="Calculate", command=self.calculator, width=20)
        self.calculate.grid(row=3, column=0, columnspan=2, pady=10)

        self.result = tk.Label(root, text="", fg="blue")
        self.result.grid(row=4, column=0, columnspan=2, pady=10)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def average(self, grades):
        return round(sum(grades) / len(grades), 2) if grades else 0

    def descriptor(self, average):
        if average > 90:
            return 'O'
        elif average >= 85:
            return 'VS'
        elif average >= 80:
            return 'S'
        elif average >= 75:
            return 'FS'
        else:
            return 'F'

    def calculator(self):
        name = self.name.get().strip()
        trasec = self.trasec.get().strip()
        tgrades = self.grades.get().strip()

        if not name or not trasec or not tgrades:
            messagebox.showerror("Error", "All fields must be filled!")
            return

        try:
            grades = [float(g) for g in tgrades.split(',') if g.strip()]
            if not grades:
                messagebox.showerror("Error", "Please enter at least one valid grade.")
                return

            if any(g < 0 or g > 100 for g in grades):
                messagebox.showerror("Error", "Grades must be between 0 and 100.")
                return

            average = self.average(grades)
            grade = self.descriptor(average)
            self.result.config(text=f"{name} from {trasec}'s average: {average:.2f} ({grade})")

        except ValueError:
            messagebox.showerror("Error", "Please enter numeric grades separated by commas.")

    def show_about(self):
        messagebox.showinfo("About", "GWA Calculator\nVersion 1.0\n© 2025 Puting Lobo Station")

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculatorGUI(root)
    root.mainloop()
