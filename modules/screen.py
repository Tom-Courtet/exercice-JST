import tkinter as tk

def get_screen_dimensions():
       root = tk.Tk()
       root.withdraw()
       screen_width = root.winfo_screenwidth()
       screen_height = root.winfo_screenheight()
       root.quit()
       return screen_width, screen_height