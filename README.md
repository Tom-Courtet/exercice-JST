# Explications exercice JST

Tom Courtet

Dans ce document, des explications concernant les trois scripts que j’ai implémenté vous aideront à comprendre mon raisonnement et le code.

# 1er Script

---

Ce script est celui qui répond au sujet de base, il utilise matplotlib pour créer une figure et créer les éléments dont on a besoin.
Il utilise la classe Rectangle que j’ai créé pour rendre le code maintenable. Cette classe a plusieurs attributs comme les coordonnées, les dimensions, la couleur et l’épaisseur de la bordure. La classe possède aussi une méthode draw qui permet d’ajouter le rectangle à notre fenêtre; elle prend en paramètres l’axe sur lequel le rectangle est dessiné, patches aui correspond aux models de figures disponibles comme les rectangles et les offset qui permettent d’espacer le cadre des axes des coordonnées.
Pour finir, on affiche aussi une grille pour avoir une meilleure visualisation des dimensions.

# 2ème script

---

Ce deuxième script est une première amélioration du premier script, il met en place la gestion automatique des couleurs de nos rectangles en utilisant colorsys. On adapte aussi la fenêtre à la taille de l’écran lors de l’ouverture pour rendre notre application plus visible lors de l’ouverture. Pour ce faire, j’utilise tkinter pour récupérer la hauteur et la largeur de l’écran. De cette manière, quand on exécute le script, la fenêtre ouverte aura une taille proportionelle à l’écran car l’application du premier script pouvait être difficilement visible en raison de la taille fixe de la fenêtre.

J’affiche aussi la barre d’outil de base de matplotlib pour permettre de bouger nos formes et zoomer.
Avec ce script, l’application est plus exploitable qu’à l’origine.

# 3ème script

---

Pour le troisième script, la principale modification du script est une amélioration du code pour la maintanbilité. 

En effet le projet est mieux organisé avec l’ajout des dossiers classes, modules et constants pour diviser le code et le rendre plus facile à maintenir.

Dans le dossier classes se trouve la classe Rectangle, dans le dossier modules se trouve le module colors qui contient la fonction random_colors pour la gestion des couleurs automatiques (elle a été modifiée pour la rendre plus stable. Il y a aussi le module screen qui contient la fonction get_screen_dimensions qui récupère les dimensions de l’écran.

Dans le dossier constants se trouve un fichier qui répertorie toutes les valeurs dont on a besoin régulièrement et qui ne changent pas comme : 

- FRAME_WIDTH : largeur du cadre
- FRAME_HEIGHT: hauteur du cadre
- X_OFFSET: décalage du cadre sur l’axe x
- Y_OFFSET: décalage du cadre sur l’axe y
- GRID_INTERVAL: espace entre les lignes de la grille en arrière plan

De cette manière, le code est beaucoup plus maintenable car chaque chose différente se trouve dans son contexte et chaque fonction n’exécute qu’une seule tâche (Single Responsibility Principle).

De plus, j’ai ajouté un bouton de changement de couleur pour permettre à l’utilisateur de changer les couleurs aléatoirement à sa guise. 

Pour ce faire, j’utilise tkinter pour ajouter notre bouton à la barre d’outils et j’ai fait une fonction update_plot qui supprime toutes les formes de notre application et les redessine toutes (ainsi que la grille de fond) avec de nouvelles couleurs.

De cette manière, l’application est utilisable et maintenable très facilement et répond aux attentes de base avec quelques améliorations.
