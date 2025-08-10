import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management App")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize tasks list
        self.tasks = []
        
        # Create main frame
        main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Welcome to the Task Management App", 
                              font=('Arial', 16, 'bold'), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=(0, 20))
        
        # Task display frame
        display_frame = tk.Frame(main_frame, bg='#f0f0f0')
        display_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        # Task listbox with scrollbar
        listbox_frame = tk.Frame(display_frame, bg='#f0f0f0')
        listbox_frame.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.task_listbox = tk.Listbox(listbox_frame, font=('Arial', 10), 
                                      yscrollcommand=scrollbar.set, height=15)
        self.task_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='#f0f0f0')
        buttons_frame.pack(fill='x', pady=10)
        
        # Create buttons
        btn_style = {'font': ('Arial', 10), 'padx': 15, 'pady': 5, 'width': 12}
        
        self.add_btn = tk.Button(buttons_frame, text="Add Task", bg='#4CAF50', 
                                fg='white', command=self.add_task, **btn_style)
        self.add_btn.pack(side='left', padx=5)
        
        self.update_btn = tk.Button(buttons_frame, text="Update Task", bg='#2196F3', 
                                   fg='white', command=self.update_task, **btn_style)
        self.update_btn.pack(side='left', padx=5)
        
        self.delete_btn = tk.Button(buttons_frame, text="Delete Task", bg='#f44336', 
                                   fg='white', command=self.delete_task, **btn_style)
        self.delete_btn.pack(side='left', padx=5)
        
        self.view_btn = tk.Button(buttons_frame, text="View All", bg='#FF9800', 
                                 fg='white', command=self.view_tasks, **btn_style)
        self.view_btn.pack(side='left', padx=5)
        
        # Initialize with some tasks (like your original code asked for initial tasks)
        self.initialize_tasks()
        
    def initialize_tasks(self):
        """Initialize app by asking for initial tasks"""
        try:
            num_tasks = simpledialog.askinteger("Initial Setup", 
                                              "Enter how many tasks you want to add:",
                                              minvalue=0, maxvalue=20)
            if num_tasks is None:
                num_tasks = 0
                
            for i in range(num_tasks):
                task = simpledialog.askstring("Task Entry", f"Enter task {i+1}:")
                if task and task.strip():
                    self.tasks.append(task.strip())
                    
            self.refresh_listbox()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def add_task(self):
        """Add a new task"""
        task = simpledialog.askstring("Add Task", "Enter task you want to add:")
        if task and task.strip():
            self.tasks.append(task.strip())
            self.refresh_listbox()
            messagebox.showinfo("Success", f"Task '{task}' has been successfully added!")
        elif task is not None:  # User clicked OK but entered empty string
            messagebox.showwarning("Warning", "Empty task not added.")
    
    def update_task(self):
        """Update an existing task"""
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks to update.")
            return
            
        # Get selected task from listbox
        selection = self.task_listbox.curselection()
        if selection:
            # Use selected task
            old_task = self.tasks[selection[0]]
        else:
            # Ask user to enter task name
            old_task = simpledialog.askstring("Update Task", 
                                            "Enter the exact task name you want to update:")
            if not old_task:
                return
                
        if old_task in self.tasks:
            new_task = simpledialog.askstring("Update Task", 
                                            f"Enter new task to replace '{old_task}':")
            if new_task and new_task.strip():
                index = self.tasks.index(old_task)
                self.tasks[index] = new_task.strip()
                self.refresh_listbox()
                messagebox.showinfo("Success", f"Updated task '{old_task}' to '{new_task}'")
            elif new_task is not None:
                messagebox.showwarning("Warning", "Empty task name not allowed.")
        else:
            messagebox.showerror("Error", f"Task '{old_task}' not found.")
    
    def delete_task(self):
        """Delete a task"""
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks to delete.")
            return
            
        # Get selected task from listbox
        selection = self.task_listbox.curselection()
        if selection:
            task_to_delete = self.tasks[selection[0]]
            self.tasks.remove(task_to_delete)
            self.refresh_listbox()
            messagebox.showinfo("Success", f"Deleted task '{task_to_delete}'")
        else:
            # Ask user to enter task name
            task_to_delete = simpledialog.askstring("Delete Task", 
                                                   "Enter the exact task name to delete:")
            if task_to_delete and task_to_delete in self.tasks:
                self.tasks.remove(task_to_delete)
                self.refresh_listbox()
                messagebox.showinfo("Success", f"Deleted task '{task_to_delete}'")
            elif task_to_delete:
                messagebox.showerror("Error", f"Task '{task_to_delete}' not found.")
    
    def view_tasks(self):
        """Display all tasks in a message box"""
        if not self.tasks:
            messagebox.showinfo("Tasks", "No tasks available.")
        else:
            tasks_text = "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])
            messagebox.showinfo("All Tasks", f"Current tasks:\n\n{tasks_text}")
    
    def refresh_listbox(self):
        """Refresh the task listbox display"""
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, 1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
