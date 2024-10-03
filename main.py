import sys
import random
import os
from PIL import Image

# SLOT GAME BY ERIC

def rzut():
    pass

def wyswieltanie():
    pass

def wyplata():
    pass

def main():
    balance = 100

    # Ścieżka do folderu z ikonami
    icons_folder = 'icons/'

    # Lista nazw plików ikon
    icon_names = ['Angular.png', 'CSS.png', 'HTML.png', 'Java.png', 'JS.png', 'PHP.png', 'PYTHON.png', 'react.png']

    print("*********************")
    print("Welcome to Slot Game by Eric")
    print("Symbols: ")
    print("*********************")

    # Ładowanie ikon
    icons = []
    for icon_name in icon_names:
        img_path = os.path.join(icons_folder, icon_name)
        img = Image.open(img_path)
        icons.append(img)

    # Wyświetlanie obrazów
    for img in icons:
        img.show()  # Wyświetla każdy obraz osobno w domyślnej przeglądarce obrazów


if __name__ == "__main__":
    main()

asdasdasdasdasdasdasdasd
asdasdasdasdas
ASdasdasdasda
