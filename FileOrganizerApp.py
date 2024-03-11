import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class FileOrganizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Organizer")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Select a folder to organize:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=10)

    def browse_folder(self):
        folder_path = filedialog.askdirectory(title="Select Folder")
        if folder_path:
            self.organize_files(folder_path)
            messagebox.showinfo("Success", "Files organized successfully!")

    def organize_files(self, folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                category = self.get_file_category(file_path)
                category_folder = os.path.join(folder_path, category)
                self.create_category_folder(folder_path, category_folder)
                self.move_file(file_path, category_folder)

    def get_file_category(self, file_path):
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension in ('.pdf', '.doc', '.docx', '.txt','.xlsx'):
            return 'Docs'
        elif file_extension in ('.jpg', '.jpeg', '.png', '.gif'):
            return 'Pictures'
        elif file_extension in ('.mp4', '.avi', '.mkv', '.mov'):
            return 'Videos'
        else:
            return 'Other'

    def create_category_folder(self, folder_path, category_folder):
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

    def move_file(self, file_path, destination_folder):
        shutil.move(file_path, destination_folder)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
