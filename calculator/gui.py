import tkinter as tk
from tkinter import messagebox
from calculator_app import perform_operations


class CalculatorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.display_label = None
        self.wm_title("Calculator App")

        container = tk.Frame(self, height=600, width=300)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.initialize_gui(container)

    def initialize_gui(self, container):
        
        self.display_label = tk.Label(container, text="" * 60, font=("Helvetica", 16), anchor="e", bg="white",
                                      relief="sunken", height=2, width=14)
        self.display_label.grid(row=0, column=1, sticky="nsew")

        self.create_keypad(container)

    # Further GUI setup and game logic will be added here
    def create_keypad(self, container):
        button_frame = tk.Frame(container)
        button_frame.grid(row=1, column=1, sticky="nsew")

        buttons = ['inv', 'abs', 'exp', 'CE',
                   'x^y', 'n!', 'log', 'Mod',
                   '7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', '.', '=', '+']

        for i, character in enumerate(buttons):
            button = tk.Button(button_frame, text=character, width=10, height=2,
                               command=lambda n=character: self.on_keypad_click(n))
            button.grid(row=i // 4, column=i % 4, padx=3, pady=3)

    def on_keypad_click(self, character):
        print(f"Button {character} clicked")
        if character == 'CE':
            self.display_label.config(text="")
        elif character == '=':
            self.calculate_result()
        elif character in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            current_text = self.display_label.cget("text")
            self.display_label.config(text=current_text + character)
        elif character == 'x^y':
            current_text = self.display_label.cget("text")
            self.display_label.config(text=current_text + " ^ ")
        else:
            current_text = self.display_label.cget("text")
            self.display_label.config(text=current_text + " " + character + " ")

    def calculate_result(self):
        try:
            expression = self.display_label.cget("text")
            if any(op in expression for op in ['abs', 'inv', 'exp', 'n!', 'log']):
                for op in ['abs', 'inv', 'exp', 'n!', 'log']:
                    if op in expression:
                        number = int(expression.replace(op, ''))
                        result = perform_operations(op, number)
                        self.display_label.config(text=str(result))
                        return
            else:
                for op in ['+', '-', '*', '/', '^', 'Mod']:
                    if op in expression:
                        parts = expression.split(op)
                        if len(parts) == 2:
                            number_1, number_2 = parts
                            number_1, number_2 = int(number_1.strip()), int(number_2.strip())
                            result = perform_operations(op, number_1, number_2)
                            self.display_label.config(text=str(result))
                            return
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            self.display_label.config(text="")
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")
            self.display_label.config(text="")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.display_label.config(text="")


def main():
    app = CalculatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
