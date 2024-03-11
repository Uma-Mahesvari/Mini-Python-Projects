import tkinter as tk
from tkinter import ttk

class InteractiveStorybookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Storybook App")

        # Set up story frames
        self.story_frames = [
            "Once upon a time, in a magical land far away...",
            "Meet our friendly dragon named Sparky!",
            "Sparky loves to fly in the sky and breathe fire.",
            "One day, Sparky discovered a hidden treasure!",
            "The treasure was filled with colorful gems and coins.",
            "And so, Sparky and the treasure lived happily ever after."
        ]

        # Create widgets
        self.create_widgets()

        # Start the story
        self.show_story_frame(0)

    def create_widgets(self):
        # Text widget for displaying the story
        self.story_text_widget = tk.Text(self.master, wrap=tk.WORD, width=60, height=15, font=("Arial", 12))
        self.story_text_widget.pack(pady=10)

        # Scrollbar for the text widget
        scrollbar = ttk.Scrollbar(self.master, command=self.story_text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.story_text_widget.config(yscrollcommand=scrollbar.set)

        # Button to navigate to the next frame
        ttk.Button(self.master, text="Next", command=self.next_story_frame).pack(pady=10)

    def show_story_frame(self, frame_index):
        # Display text
        self.story_text_widget.delete(1.0, tk.END)
        self.story_text_widget.insert(tk.END, self.story_frames[frame_index])

    def next_story_frame(self):
        # Move to the next frame in the story
        current_frame_index = self.story_frames.index(self.story_text_widget.get(1.0, tk.END).strip())
        next_frame_index = current_frame_index + 1

        if next_frame_index < len(self.story_frames):
            self.show_story_frame(next_frame_index)
        else:
            # End of the story
            ttk.Label(self.master, text="The end!", font=("Arial", 16, "bold")).pack(pady=20)
            ttk.Button(self.master, text="Close", command=self.master.destroy).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveStorybookApp(root)
    root.mainloop()
