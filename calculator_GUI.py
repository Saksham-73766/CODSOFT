import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')
        
        # Main frame
        main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Simple Calculator", 
                              font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#f0f0f0')
        input_frame.pack(fill='x', pady=10)
        
        # First number
        tk.Label(input_frame, text="First Number:", font=('Arial', 12), 
                bg='#f0f0f0').grid(row=0, column=0, sticky='w', pady=5)
        self.num1_entry = tk.Entry(input_frame, font=('Arial', 12), width=15)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Second number
        tk.Label(input_frame, text="Second Number:", font=('Arial', 12), 
                bg='#f0f0f0').grid(row=1, column=0, sticky='w', pady=5)
        self.num2_entry = tk.Entry(input_frame, font=('Arial', 12), width=15)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Operation buttons frame
        operations_frame = tk.Frame(main_frame, bg='#f0f0f0')
        operations_frame.pack(pady=20)
        
        # Operation buttons
        btn_style = {'font': ('Arial', 14, 'bold'), 'width': 3, 'height': 2}
        
        self.add_btn = tk.Button(operations_frame, text="+", bg='#4CAF50', 
                                fg='white', command=lambda: self.calculate('+'), **btn_style)
        self.add_btn.grid(row=0, column=0, padx=5, pady=5)
        
        self.sub_btn = tk.Button(operations_frame, text="-", bg='#2196F3', 
                                fg='white', command=lambda: self.calculate('-'), **btn_style)
        self.sub_btn.grid(row=0, column=1, padx=5, pady=5)
        
        self.mul_btn = tk.Button(operations_frame, text="×", bg='#FF9800', 
                                fg='white', command=lambda: self.calculate('*'), **btn_style)
        self.mul_btn.grid(row=1, column=0, padx=5, pady=5)
        
        self.div_btn = tk.Button(operations_frame, text="÷", bg='#f44336', 
                                fg='white', command=lambda: self.calculate('/'), **btn_style)
        self.div_btn.grid(row=1, column=1, padx=5, pady=5)
        
        # Result display
        result_frame = tk.Frame(main_frame, bg='#f0f0f0')
        result_frame.pack(fill='x', pady=20)
        
        tk.Label(result_frame, text="Result:", font=('Arial', 12, 'bold'), 
                bg='#f0f0f0').pack()
        
        self.result_label = tk.Label(result_frame, text="", font=('Arial', 14), 
                                    bg='white', relief='sunken', height=2, width=30)
        self.result_label.pack(pady=10)
        
        # Clear button
        clear_btn = tk.Button(main_frame, text="Clear", font=('Arial', 12), 
                             bg='#9E9E9E', fg='white', command=self.clear_fields,
                             width=10, height=1)
        clear_btn.pack(pady=10)
        
    def calculate(self, operation):
        try:
            # Get input values
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            
            # Perform calculation
            if operation == '+':
                result = num1 + num2
                op_symbol = '+'
            elif operation == '-':
                result = num1 - num2
                op_symbol = '-'
            elif operation == '*':
                result = num1 * num2
                op_symbol = '×'
            elif operation == '/':
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = num1 / num2
                op_symbol = '÷'
            
            # Display result
            result_text = f"{num1} {op_symbol} {num2} = {result}"
            self.result_label.config(text=result_text)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def clear_fields(self):
        """Clear all input fields and result"""
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
