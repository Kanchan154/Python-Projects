import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = 'main.json'


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1)

        self.listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack(pady=5)

        self.done_btn = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.done_btn.pack(pady=5)

        self.update_listbox()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            save_tasks(self.tasks)
            self.task_entry.delete(0, tk.END)
            self.update_listbox()

    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            save_tasks(self.tasks)
            self.update_listbox()

    def mark_done(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["done"] = True
            save_tasks(self.tasks)
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display = f"[{'✅' if task['done'] else '❌'}] {task['task']}"
            self.listbox.insert(tk.END, display)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
