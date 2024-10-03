from setting import *
from reel import *
import pygame

class Machine:
        # WYSWIETLANIE SAMEGO EKRANU
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_list = {}  # Tworzy pusty słownik, który będzie przechowywać bębny (reels)
        self.reel_index = 0 # Inicjalizuje indeks bębna, zaczynając od 0

        self.spawn_reels() # Wywołuje metodę, która generuje i wyświetla bębny

    def spawn_reels(self): # FUNKCJA DO WYSWIETLANIA ICH NA EKRANIE
        if not self.reel_list: # Sprawdza, czy lista bębnów jest pusta
            x_topleft, y_topleft = 10, -300 # Ustawia początkową pozycję pierwszego bębna na ekranie (10, -300)
        while self.reel_index < 5:  # Pętla działa, dopóki nie zostanie utworzone 5 bębnów
            if self.reel_index > 0:  # Jeśli to nie pierwszy bęben
                x_topleft, y_topleft = x_topleft + (
                            300 + X_OFFSET), y_topleft  # Przesuwa bęben w poziomie o 300 pikseli + wartość X_OFFSET

            self.reel_list[self.reel_index] = Reel(
                (x_topleft, y_topleft))  # Tworzy nowy bęben i dodaje go do listy bębnów pod odpowiednim indeksem
            self.reel_index += 1  # Zwiększa indeks bębna o 1, aby przygotować miejsce na kolejny

    def update(self, delta_time):  # Funkcja aktualizująca stan bębnów w czasie gry
        for reel in self.reel_list:  # Iteruje przez wszystkie bębny w liście bębnów
            self.reel_list[reel].symbol_list.draw(self.display_surface)  # Rysuje symbole na ekranie (display_surface) dla każdego bębna
            self.reel_list[reel].symbol_list.update()  # Aktualizuje stan każdego symbolu na bębnie (np. animacje, pozycje)
