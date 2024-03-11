import pandas as pd
from prettytable import PrettyTable
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

class MonthlyAttendanceTracker:
    def __init__(self, excel_file="attendance_records.xlsx"):
        self.excel_file = excel_file
        self.attendance = self.load_attendance()

    def mark_attendance(self, student_id, name, date, status):
        student_key = f"{student_id}-{name}"

        if student_key not in self.attendance:
            self.attendance[student_key] = {date: status}
        elif date not in self.attendance[student_key]:
            self.attendance[student_key][date] = status
            print(f"{name} marked {status} on {date}.")
        else:
            print(f"{name} already has {status} recorded on {date}.")

    def calculate_percentage(self, student_name):
        total_days = len(self.attendance[student_name])
        present_days = sum(1 for date_attendance in self.attendance[student_name].values() if date_attendance == "Present")
        if total_days > 0:
            percentage = (present_days / total_days) * 100
            return percentage
        return 0

    def display_attendance_table(self,student_id, name, date, status):
        table = PrettyTable()
        table.field_names = ["Student ID", "Name", "Date", "Attendance Status"]

        table.add_row([student_id, name, date, status])

        return table

    def save_attendance(self,student_id, name, date, status):
        df_list = []
        df_list.append([student_id, name, date, status])

        df = pd.DataFrame(df_list, columns=["Student ID", "Name", "Date", "Attendance Status"])

        try:
            existing_df = pd.read_excel(self.excel_file)

            # Remove header from new data frame to avoid duplication
            df_no_header = df.iloc[1:, :]  # Assuming the first row is a header

            # Append new data to existing data frame
            combined_df = pd.concat([existing_df, df], ignore_index=True)

            # Save the combined data frame to the Excel file
            combined_df.to_excel(self.excel_file, index=False)
            print(combined_df)

            print("Updated Excel")
        except FileNotFoundError:
            df.to_excel(self.excel_file, index=False)
            print("New Excel file created with attendance data.")



    def load_attendance(self):
        try:
            df = pd.read_excel(self.excel_file)
            return df.to_dict(orient="index")
        except FileNotFoundError:
            return {}

class AttendanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Monthly Attendance Tracker")

        self.attendance_tracker = MonthlyAttendanceTracker()

        self.create_widgets()

    def create_widgets(self):
        # Entry fields
        tk.Label(self.root, text="Student ID:").grid(row=0, column=0, padx=5, pady=5)
        self.student_id_entry = tk.Entry(self.root)
        self.student_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Calendar for selecting date
        tk.Label(self.root, text="Select Date:").grid(row=2, column=0, padx=5, pady=5)
        self.date_cal = Calendar(self.root, selectmode="day", date_pattern="yyyy-mm-dd", year=2024, month=3, day=5,maxdate=datetime.today())
        self.date_cal.grid(row=2, column=1, padx=5, pady=5)

        # Attendance Status dropdown
        tk.Label(self.root, text="Attendance Status:").grid(row=3, column=0, padx=5, pady=5)
        self.status_var = tk.StringVar()
        self.status_combobox = ttk.Combobox(self.root, textvariable=self.status_var, values=["Present", "Absent"])
        self.status_combobox.grid(row=3, column=1, padx=5, pady=5)
        self.status_combobox.set("Present")  # Default value

        # Clear button
        clear_button = tk.Button(self.root, text="Clear Data", command=self.clear_entries)
        clear_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # Buttons
        mark_button = tk.Button(self.root, text="Mark Attendance", command=self.mark_attendance)
        mark_button.grid(row=4, column=0, columnspan=2, pady=10)

        display_button = tk.Button(self.root, text="Display Attendance Table", command=self.display_attendance)
        display_button.grid(row=5, column=0, columnspan=2, pady=10)

        save_button = tk.Button(self.root, text="Save Attendance", command=self.save_attendance)
        save_button.grid(row=6, column=0, columnspan=2, pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)


    def clear_entries(self):
        # Clear entry fields and reset calendar
        self.student_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.status_combobox.set("Present")  # Reset to default value
        
    def mark_attendance(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        date = self.date_cal.get_date()
        status = self.status_var.get()  # Get the selected status from the Combobox

        self.attendance_tracker.mark_attendance(student_id, name, date, status)

    def display_attendance(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        date = self.date_cal.get_date()
        status = self.status_var.get()  # Get the selected status from the Combobox
        table = self.attendance_tracker.display_attendance_table(student_id, name, date, status)
        self.display_table_window(table)

    def save_attendance(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        date = self.date_cal.get_date()
        status = self.status_var.get()  # Get the selected status from the Combobox
        self.attendance_tracker.save_attendance(student_id, name, date, status)

    def display_table_window(self, table):
        table_window = tk.Toplevel(self.root)
        table_window.title("Attendance Table")

        tree = ttk.Treeview(table_window)
        tree["columns"] = table.field_names

        for col in table.field_names:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        for row in table._rows:
            tree.insert("", "end", values=row)

        tree.pack(expand=tk.YES, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceGUI(root)
    root.mainloop()
