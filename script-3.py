# *****************************************
# *                                       *
# *          Auteur: Tom Courtet          *
# *                                       *
# * Exercice fait pour JST Transformateur *
# *                                       *
# *****************************************



from constants.constants import FRAME_WIDTH, FRAME_HEIGHT, X_OFFSET, Y_OFFSET, GRID_INTERVAL
from modules.colors import random_color
from modules.screen import get_screen_dimensions
from classes.Rectangle import Rectangle
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk

def create_figures_and_axes(screen_width, screen_height):
    fig, ax = plt.subplots()
    fig.set_size_inches(screen_width / 100, screen_height / 100)
    ax.set_xlim(0, FRAME_WIDTH + X_OFFSET + GRID_INTERVAL)
    ax.set_ylim(0, FRAME_HEIGHT + Y_OFFSET + GRID_INTERVAL)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xticks(range(0, FRAME_WIDTH + X_OFFSET + GRID_INTERVAL, GRID_INTERVAL))
    ax.set_yticks(range(0, FRAME_HEIGHT + Y_OFFSET + GRID_INTERVAL, GRID_INTERVAL))
    return fig, ax

def draw_rectangles(ax, rectangles):
    for rect in rectangles:
        rect.color = random_color()
        rect.draw(ax, patches, X_OFFSET, Y_OFFSET)

class CustomToolbar(NavigationToolbar2Tk):
    def __init__(self, canvas, root, rectangles, ax, cadre):
        self.rectangles = rectangles
        self.ax = ax
        self.cadre = cadre
        self.canvas = canvas
        super().__init__(canvas, root)
        self.add_custom_button()

    def add_custom_button(self):
        # Ajouter le bouton à la barre d'outils
        self.custom_button = tk.Button(
            self, text="Changer Couleurs", command=self.on_button_click
        )
        self.custom_button.pack(side=tk.LEFT, padx=2, pady=2)

    def on_button_click(self):
        for rect in self.rectangles:
            rect.color = random_color()
        self.update_colors()

    def update_colors(self):
        for rect in self.rectangles:
            rect.draw(self.ax, patches, X_OFFSET, Y_OFFSET)
        self.canvas.draw()

def main():
    screen_width, screen_height = get_screen_dimensions()
    fig, ax = create_figures_and_axes(screen_width, screen_height)
    
    cadre = Rectangle(0, 0, FRAME_WIDTH, FRAME_HEIGHT, 'none', 2)
    cadre.draw(ax, patches, X_OFFSET, Y_OFFSET)
    
    rectangles = [
        Rectangle(20, 70, 100, 1200, None),
        Rectangle(150, 120, 250, 1100, None),
        Rectangle(412, 170, 100, 1000, None)
    ]
    
    draw_rectangles(ax, rectangles)
    
    root = tk.Tk()
    root.title("Projet JST")
    
    # Créer un cadre pour organiser les widgets
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Utiliser la barre d'outils personnalisée
    toolbar = CustomToolbar(canvas, frame, rectangles, ax, cadre)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.X)
    
    # Assurer que le script se termine correctement lorsque la fenêtre est fermée
    def on_closing():
        root.quit()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    plt.gca().set_aspect('equal', adjustable='box')
    root.mainloop()

if __name__ == "__main__":
    main()