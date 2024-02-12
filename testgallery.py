import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

# Specify the directory containing the photos
photo_dir = "licet_photo"

# Get a list of all the photo file names in the directory
photo_files = [f for f in os.listdir(photo_dir) if f.endswith(".JPG")]

class PhotoGallery:
    def __init__(self, master, photo_files):
        self.master = master
        self.photo_files = photo_files
        self.current_photo_index = 0
        
        # Create the scrollable canvas to display the photos
        self.canvas = tk.Canvas(self.master, width=700, height=690)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.bind("<Configure>", self.resize_canvas)

        
        # Create a frame to contain the photo labels
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw")
        
        # Create the navigation buttons
        self.prev_button = ttk.Button(self.master, text="Prev", command=self.show_prev_photo)
        self.prev_button.pack(side="left")
        self.next_button = ttk.Button(self.master, text="Next", command=self.show_next_photo)
        self.next_button.pack(side="right")
        
        # Create the photo label in the main window
        self.photo_label = ttk.Label(self.master)
        self.photo_label.pack(fill="both", expand=True)
        
        # Load and display all the photos in the canvas grid layout
        self.photo_labels = []
        for i, photo_file in enumerate(self.photo_files):
            photo = Image.open(os.path.join(photo_dir, photo_file))
            photo = photo.resize((200, 150))
            photo_tk = ImageTk.PhotoImage(photo)
            label = ttk.Label(self.frame, image=photo_tk)
            label.image = photo_tk
            label.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            label.bind("<Button-1>", lambda event, index=i: self.select_photo(index))
            self.photo_labels.append(label)
        
        # Select the first photo
        self.select_photo(0)
        
        # Create the vertical scrollbar for the canvas
        self.v_scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.v_scrollbar.pack(side="left", fill="y")
        self.canvas.config(yscrollcommand=self.v_scrollbar.set)
        
        # Bind the canvas to keyboard events
        self.canvas.bind("<Up>", self.scroll_up)
        self.canvas.bind("<Down>", self.scroll_down)
        
    def resize_canvas(self, event):
        # Resize the canvas and update the scrollbar
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
    def select_photo(self, index):
        # Deselect the current photo
        if self.current_photo_index is not None:
            self.photo_labels[self.current_photo_index].configure(relief="flat")
        
        # Select the new photo
        self.current_photo_index = index
        self.photo_labels[self.current_photo_index].configure(relief="solid")
        
        # Update the photo label in the main window
        photo_file = os.path.join(photo_dir, self.photo_files[self.current_photo_index])
        photo = Image.open(photo_file)
        photo = photo.resize((500, 400))
        photo_tk = ImageTk.PhotoImage(photo)
        self.photo_label.configure(image=photo_tk)
        self.photo_label.image = photo_tk

        
    def scroll_up(self, event):
        self.canvas.yview_scroll(-1, "units")
        
    def scroll_down(self, event):
        self.canvas.yview_scroll(1, "units")
    def show_prev_photo(self):
        # Decrement the current photo index and select the new photo
        self.select_photo((self.current_photo_index - 1) % len(self.photo_files))

    def show_next_photo(self):
        # Increment the current photo index and select the new photo
        self.select_photo((self.current_photo_index + 1) % len(self.photo_files))
# Create the main window and set its title
root = tk.Tk()
root.title("Photo Gallery")

# Create the photo gallery and start the main event loop
photo_gallery = PhotoGallery(root, photo_files)
root.mainloop()

#add scrolling and key stroke feature
