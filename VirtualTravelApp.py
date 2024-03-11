import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class VirtualTravelApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual Travel Experience")

        # Dictionary to store virtual travel destinations
        self.destinations = {
            "Paris": "paris.jpg",
            "Tokyo": "tokyo.jpg",
            "New York": "new_york.jpg",
            "Rome": "rome.jpg",
            # Add more destinations as needed
        }

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Dropdown for selecting destinations
        tk.Label(self.master, text="Select a Destination:").pack(pady=10)
        self.destination_var = tk.StringVar()
        self.destination_dropdown = ttk.Combobox(self.master, textvariable=self.destination_var, values=list(self.destinations.keys()), state="readonly")
        self.destination_dropdown.set("Paris")  # Default destination
        self.destination_dropdown.pack(pady=10)

        # Button to start the virtual travel
        tk.Button(self.master, text="Start Virtual Travel", command=self.start_virtual_travel).pack(pady=20)

        # Canvas to display destination images
        self.canvas = tk.Canvas(self.master, width=800, height=500)
        self.canvas.pack()

    def start_virtual_travel(self):
        selected_destination = self.destination_var.get()

        if selected_destination in self.destinations:
            image_path = self.destinations[selected_destination]
            self.display_destination_image(image_path)
        else:
            messagebox.showwarning("Invalid Destination", "Please select a valid destination.")

    def display_destination_image(self, image_path):
        try:
            image = Image.open(image_path)
            image = image.resize((800, 500))
            photo = ImageTk.PhotoImage(image)

            # Clear previous image on the canvas
            self.canvas.delete("all")

            # Display the new image on the canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualTravelApp(root)
    root.mainloop()
