
# *****************************************
# *                                       *
# *          Auteur: Tom Courtet          *
# *                                       *
# * Exercice fait pour JST Transformateur *
# *                                       *
# *****************************************



import matplotlib.pyplot as plt
import matplotlib.patches as patches
from classes.Rectangle import Rectangle


# Dimensions du cadre
cadre_largeur = 550
cadre_hauteur = 1340

# Espacement par rapport à la bordure 
x_offset = 250
y_offset = 0

# Dimensions et positions des rectangles
rectangles = [
    Rectangle(20, 70, 100, 1200, 'r'),
    Rectangle(150, 120, 250, 1100, 'b'),
    Rectangle(412, 170, 100, 1000, 'g')
]

# Création de la figure et des axes
fig, ax = plt.subplots()

# Définir les limites des axes
ax.set_xlim(0, cadre_largeur + x_offset + 100)
ax.set_ylim(0, cadre_hauteur + y_offset + 100)

# Ajouter une grille avec des intervalles spécifiques
ax.grid(True)
ax.set_axisbelow(True)
ax.set_xticks(range(0, cadre_largeur + x_offset + 100, 100))
ax.set_yticks(range(0, cadre_hauteur + y_offset + 100, 100))


# Dessiner le cadre horizontal
cadre = Rectangle(0,0, cadre_largeur, cadre_hauteur, 'none')
cadre.draw(ax, patches, x_offset, y_offset)

# Dessiner les rectangles avec les unités d'axe spécifiées
for rect in rectangles:
    rect.draw(ax, patches, x_offset, y_offset)


# Retrait de la barre  de menu
figManager = plt.get_current_fig_manager()
figManager.toolbar.pack_forget() 

plt.gca().set_aspect('equal', adjustable='box')
plt.show(block=True)