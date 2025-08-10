import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import pyperclip  # For copying to clipboard (pip install pyperclip)

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')
        
        # Main frame
        main_frame = tk.Frame(root, bg='#f0f0f0', padx=30, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Password Generator", 
                              font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=(0, 30))
        
        # Password length frame
        length_frame = tk.Frame(main_frame, bg='#f0f0f0')
        length_frame.pack(fill='x', pady=10)
        
        tk.Label(length_frame, text="Password Length:", font=('Arial', 12, 'bold'), 
                bg='#f0f0f0').pack(anchor='w')
        
        self.length_var = tk.StringVar(value="12")
        length_spinbox = tk.Spinbox(length_frame, from_=4, to=50, width=10, 
                                   font=('Arial', 12), textvariable=self.length_var)
        length_spinbox.pack(anchor='w', pady=5)
        
        # Complexity options frame
        complexity_frame = tk.LabelFrame(main_frame, text="Password Complexity", 
                                        font=('Arial', 12, 'bold'), bg='#f0f0f0', 
                                        padx=10, pady=10)
        complexity_frame.pack(fill='x', pady=20)
        
        # Checkboxes for character types
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        tk.Checkbutton(complexity_frame, text="Lowercase letters (a-z)", 
                      variable=self.lowercase_var, font=('Arial', 10), 
                      bg='#f0f0f0').pack(anchor='w', pady=2)
        
        tk.Checkbutton(complexity_frame, text="Uppercase letters (A-Z)", 
                      variable=self.uppercase_var, font=('Arial', 10), 
                      bg='#f0f0f0').pack(anchor='w', pady=2)
        
        tk.Checkbutton(complexity_frame, text="Numbers (0-9)", 
                      variable=self.digits_var, font=('Arial', 10), 
                      bg='#f0f0f0').pack(anchor='w', pady=2)
        
        tk.Checkbutton(complexity_frame, text="Symbols (!@#$%^&*)", 
                      variable=self.symbols_var, font=('Arial', 10), 
                      bg='#f0f0f0').pack(anchor='w', pady=2)
        
        # Preset buttons frame
        preset_frame = tk.Frame(main_frame, bg='#f0f0f0')
        preset_frame.pack(fill='x', pady=10)
        
        tk.Label(preset_frame, text="Quick Presets:", font=('Arial', 10, 'bold'), 
                bg='#f0f0f0').pack(anchor='w')
        
        preset_btn_frame = tk.Frame(preset_frame, bg='#f0f0f0')
        preset_btn_frame.pack(fill='x', pady=5)
        
        tk.Button(preset_btn_frame, text="Simple", command=self.set_simple, 
                 bg='#4CAF50', fg='white', font=('Arial', 9)).pack(side='left', padx=5)
        tk.Button(preset_btn_frame, text="Medium", command=self.set_medium, 
                 bg='#FF9800', fg='white', font=('Arial', 9)).pack(side='left', padx=5)
        tk.Button(preset_btn_frame, text="Strong", command=self.set_strong, 
                 bg='#f44336', fg='white', font=('Arial', 9)).pack(side='left', padx=5)
        
        # Generate button
        generate_btn = tk.Button(main_frame, text="Generate Password", 
                               command=self.generate_password, bg='#2196F3', 
                               fg='white', font=('Arial', 14, 'bold'), 
                               pady=10, width=20)
        generate_btn.pack(pady=20)
        
        # Result frame
        result_frame = tk.LabelFrame(main_frame, text="Generated Password", 
                                   font=('Arial', 12, 'bold'), bg='#f0f0f0', 
                                   padx=10, pady=10)
        result_frame.pack(fill='x', pady=10)
        
        # Password display
        self.password_text = tk.Text(result_frame, height=3, font=('Courier', 12), 
                                   wrap='word', state='disabled')
        self.password_text.pack(fill='x', pady=5)
        
        # Action buttons
        action_frame = tk.Frame(result_frame, bg='#f0f0f0')
        action_frame.pack(fill='x', pady=5)
        
        self.copy_btn = tk.Button(action_frame, text="Copy to Clipboard", 
                                 command=self.copy_password, bg='#9C27B0', 
                                 fg='white', font=('Arial', 10), state='disabled')
        self.copy_btn.pack(side='left', padx=5)
        
        self.clear_btn = tk.Button(action_frame, text="Clear", 
                                  command=self.clear_password, bg='#9E9E9E', 
                                  fg='white', font=('Arial', 10), state='disabled')
        self.clear_btn.pack(side='left', padx=5)
        
        # Store current password for copying
        self.current_password = ""
    
    def set_simple(self):
        """Set simple preset: letters only"""
        self.lowercase_var.set(True)
        self.uppercase_var.set(True)
        self.digits_var.set(False)
        self.symbols_var.set(False)
    
    def set_medium(self):
        """Set medium preset: letters + numbers"""
        self.lowercase_var.set(True)
        self.uppercase_var.set(True)
        self.digits_var.set(True)
        self.symbols_var.set(False)
    
    def set_strong(self):
        """Set strong preset: all character types"""
        self.lowercase_var.set(True)
        self.uppercase_var.set(True)
        self.digits_var.set(True)
        self.symbols_var.set(True)
    
    def generate_password(self):
        try:
            # Get password length
            length = int(self.length_var.get())
            
            if length < 4:
                messagebox.showwarning("Warning", "Password length should be at least 4 characters!")
                return
            
            # Build character pool
            char_pool = ""
            
            if self.lowercase_var.get():
                char_pool += string.ascii_lowercase
            if self.uppercase_var.get():
                char_pool += string.ascii_uppercase
            if self.digits_var.get():
                char_pool += string.digits
            if self.symbols_var.get():
                char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            if not char_pool:
                messagebox.showerror("Error", "Please select at least one character type!")
                return
            
            # Generate password
            password = ''.join(random.choice(char_pool) for _ in range(length))
            self.current_password = password
            
            # Display password
            self.password_text.config(state='normal')
            self.password_text.delete(1.0, tk.END)
            self.password_text.insert(1.0, f"Password: {password}\n")
            self.password_text.insert(tk.END, f"Length: {length} characters\n")
            self.password_text.insert(tk.END, f"Strength: {self.get_strength_description()}")
            self.password_text.config(state='disabled')
            
            # Enable action buttons
            self.copy_btn.config(state='normal')
            self.clear_btn.config(state='normal')
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def get_strength_description(self):
        """Get description of password strength based on selected options"""
        types = []
        if self.lowercase_var.get():
            types.append("lowercase")
        if self.uppercase_var.get():
            types.append("uppercase")
        if self.digits_var.get():
            types.append("numbers")
        if self.symbols_var.get():
            types.append("symbols")
        
        if len(types) == 1:
            return "Weak"
        elif len(types) == 2:
            return "Medium"
        elif len(types) == 3:
            return "Strong"
        else:
            return "Very Strong"
    
    def copy_password(self):
        """Copy password to clipboard"""
        try:
            pyperclip.copy(self.current_password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except:
            # Fallback if pyperclip is not installed
            self.root.clipboard_clear()
            self.root.clipboard_append(self.current_password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
    
    def clear_password(self):
        """Clear the password display"""
        self.password_text.config(state='normal')
        self.password_text.delete(1.0, tk.END)
        self.password_text.config(state='disabled')
        self.current_password = ""
        self.copy_btn.config(state='disabled')
        self.clear_btn.config(state='disabled')

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
