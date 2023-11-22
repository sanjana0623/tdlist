#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
import json

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.description_entry = tk.Entry(root, width=50)
        self.description_entry.grid(row=0, column=0, padx=10, pady=10)

        self.due_date_entry = tk.Entry(root, width=15)
        self.due_date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.due_date_entry.insert(0, "Due Date")

        self.priority_entry = tk.Entry(root, width=15)
        self.priority_entry.grid(row=0, column=2, padx=10, pady=10)
        self.priority_entry.insert(0, "Priority")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=3, padx=10, pady=10)

        self.task_list = ttk.Treeview(root, columns=("Description", "Priority", "Due Date", "Status"), show="headings")
        self.task_list.heading("Description", text="Description")
        self.task_list.heading("Priority", text="Priority")
        self.task_list.heading("Due Date", text="Due Date")
        self.task_list.heading("Status", text="Status")
        self.task_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_as_complete)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=10, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=2, padx=10, pady=10)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=3, column=0, padx=10, pady=10)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=3, column=1, padx=10, pady=10)

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if description:
            if not due_date:
                due_date = "N/A"
            if not priority:
                priority = "N/A"

            status = "Not Completed"
            self.tasks.append((description, priority, due_date, status))
            self.update_task_list()
            self.clear_entry_fields()

    def clear_entry_fields(self):
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def update_task_list(self):
        self.task_list.delete(*self.task_list.get_children())
        for task in self.tasks:
            self.task_list.insert("", tk.END, values=task)

    def mark_as_complete(self):
        selected_item = self.task_list.selection()
        if selected_item:
            index = self.task_list.index(selected_item)
            self.tasks[index] = (*self.tasks[index][:3], "Completed")
            self.update_task_list()

    def update_task(self):
        selected_item = self.task_list.selection()
        if selected_item:
            index = self.task_list.index(selected_item)
            description = self.description_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()
            
            if not due_date:
                due_date = "N/A"
            if not priority:
                priority = "N/A"

            self.tasks[index] = (description, priority, due_date, self.tasks[index][3])
            self.update_task_list()
            self.clear_entry_fields()

    def remove_task(self):
        selected_item = self.task_list.selection()
        if selected_item:
            index = self.task_list.index(selected_item)
            del self.tasks[index]
            self.update_task_list()

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
            print("Tasks saved to 'tasks.json'.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
                self.update_task_list()
                print("Tasks loaded from 'tasks.json'.")
        except FileNotFoundError:
            print("File 'tasks.json' not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()


# In[ ]:




