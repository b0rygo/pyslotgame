from setting import *
import pygame, random

class Reel:
    def __init__(self, pos):  # Konstruktor klasy Reel, przyjmujący argument `pos`, czyli pozycję na ekranie
        self.symbol_list = pygame.sprite.Group()  # Tworzy grupę (listę) symboli (używając Pygame, aby później móc nimi zarządzać)
        self.shuffled_keys = list(symbols.keys())  # Pobiera wszystkie klucze (nazwy symboli) ze słownika `symbols` i zamienia je na listę
        random.shuffle(self.shuffled_keys)  # Tasuje listę kluczy, aby symbole pojawiały się w losowej kolejności
        self.shuffled_keys = self.shuffled_keys[:5]  # Ogranicza liczbę symboli na bębnie do 5 (pierwsze 5 elementów)

        self.reel_is_spinning = False

        for idx, item in enumerate(self.shuffled_keys):  # Iteruje przez wylosowane symbole, przypisując im indeksy
            self.symbol_list.add(Symbol(symbols[item], pos, idx))  # Dodaje nowy obiekt Symbol do listy symboli, przekazując ścieżkę do pliku, pozycję i indeks
            pos = list(pos)  # Zamienia krotkę `pos` na listę (aby była modyfikowalna)
            pos[1] += 300  # Przesuwa każdy kolejny symbol w dół o 300 pikseli
            pos = tuple(pos)  # Ponownie zamienia `pos` na krotkę (bo Pygame wymaga krotek dla pozycji)

class Symbol(pygame.sprite.Sprite):  # Definicja klasy Symbol, dziedziczącej po klasie pygame.sprite.Sprite
    def __init__(self, pathToFile, pos, idx):  # Konstruktor klasy Symbol, przyjmujący ścieżkę do pliku, pozycję i indeks
        super().__init__()  # Wywołanie konstruktora klasy bazowej (pygame.sprite.Sprite)

        self.sym_type = pathToFile.split('/')[0]  # Rozdziela ścieżkę do pliku po znakach '/', aby uzyskać nazwę typu symbolu (tu pierwszy element)

        self.pos = pos  # Przechowuje pozycję symbolu
        self.idx = idx  # Przechowuje indeks symbolu (numer kolejności na bębnie)
        self.image = pygame.image.load(pathToFile).convert_alpha()  # Ładuje obraz symbolu z pliku i konwertuje go na format z przezroczystością (alpha)
        self.rect = self.image.get_rect(topleft=pos)  # Tworzy prostokąt (rect) z pozycją obrazu na ekranie (topleft określa górny-lewy róg)
        self.x_val = self.rect.left  # Przechowuje wartość pozycji poziomej (x) lewego boku symbolu

    def update(self):
        pass
