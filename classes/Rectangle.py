class Rectangle:
    def __init__(self, x, y, largeur, hauteur, color, border_width=1):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.color = color
        self.border_width = border_width

    def draw(self, ax, patches, x_offset, y_offset):
        ax.add_patch(patches.Rectangle((self.x + x_offset, self.y + y_offset), self.largeur, self.hauteur, linewidth=self.border_width, edgecolor='black', facecolor=self.color))