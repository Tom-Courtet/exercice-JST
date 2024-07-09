# *****************************************
# *                                       *
# *          Auteur: Tom Courtet          *
# *                                       *
# * Exercice fait pour JST Transformateur *
# *                                       *
# *****************************************

#
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from classes.Rectangle import Rectangle
import tkinter as tk
import random
import colorsys

# Obtenir les dimensions de l'écran
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Dimensions du cadre
cadre_largeur = 550
cadre_hauteur = 1340

# Espacement par rapport à la bordure 
x_offset = 250
y_offset = 0

# Dimensions et positions des rectangles
rectangles = [
    Rectangle(20, 70, 100, 1200, None),
    Rectangle(150, 120, 250, 1100, None),
    Rectangle(412, 170, 100, 1000, None)
]

# Fonction pour générer une couleur hexadécimale aléatoire mais distincte
def random_color():
    h = random.random()
    s = 0.5 + random.random() / 2
    v = 0.7 + random.random() / 3
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255)).upper()

# Création de la figure et des axes
fig, ax = plt.subplots()

# Définir la taille de la figure en fonction de la taille de l'écran
fig.set_size_inches(screen_width / 100, screen_height / 100)

# Définir les limites des axes
ax.set_xlim(0, cadre_largeur + x_offset + 100)
ax.set_ylim(0, cadre_hauteur + y_offset + 100)

# Ajouter une grille avec des intervalles spécifiques
ax.grid(True)
ax.set_axisbelow(True)
ax.set_xticks(range(0, cadre_largeur + x_offset + 100, 100))
ax.set_yticks(range(0, cadre_hauteur + y_offset + 100, 100))

# Dessiner le cadre horizontal
cadre = Rectangle(0, 0, cadre_largeur, cadre_hauteur, 'none', 2)
cadre.draw(ax, patches, x_offset, y_offset)

# Dessiner les rectangles avec les unités d'axe spécifiées
for rect in rectangles:
    rect.color = random_color()  # Assigner une couleur aléatoire mais distincte au rectangle
    rect.draw(ax, patches, x_offset, y_offset)

plt.gca().set_aspect('equal', adjustable='box')
plt.show(block=True)