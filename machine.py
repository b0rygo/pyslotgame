from setting import *
from reel import *
import pygame

class Machine:
        # WYSWIETLANIE SAMEGO EKRANU
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_list = {}  # Tworzy pusty słownik, który będzie przechowywać bębny (reels)
        self.reel_index = 0 # Inicjalizuje indeks bębna, zaczynając od 0
        self.can_toggle = True
        self.spinning = False

        self.spawn_reels() # Wywołuje metodę, która generuje i wyświetla bębny

    def cooldowns(self):
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = False

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True


    def input(self):
        keys = pygame.key.get_pressed()

        #if keys[pygame.K_SPACE] and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
        if keys[pygame.K_SPACE]:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            ##self.currPlayer.place_bet()
            ##self.machine_balance += self.currPlayer.bet_size
            ##self.currPlayer.last_payout = None

    def draw_reels(self,delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self): # FUNKCJA DO WYSWIETLANIA ICH NA EKRANIE
        if not self.reel_list: # Sprawdza, czy lista bębnów jest pusta
            x_topleft, y_topleft = 10, -300 # Ustawia początkową pozycję pierwszego bębna na ekranie (10, -300)
        while self.reel_index < 5:  # Pętla działa, dopóki nie zostanie utworzone 5 bębnów
            if self.reel_index > 0:  # Jeśli to nie pierwszy bęben
                x_topleft, y_topleft = x_topleft + (300 + X_OFFSET), y_topleft  # Przesuwa bęben w poziomie o 300 pikseli + wartość X_OFFSET

            self.reel_list[self.reel_index] = Reel(
                (x_topleft, y_topleft))  # Tworzy nowy bęben i dodaje go do listy bębnów pod odpowiednim indeksem
            self.reel_index += 1  # Zwiększa indeks bębna o 1, aby przygotować miejsce na kolejny

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel)*200)


    def update(self, delta_time):  # Funkcja aktualizująca stan bębnów w czasie gry
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:  # Iteruje przez wszystkie bębny w liście bębnów
            self.reel_list[reel].symbol_list.draw(self.display_surface)  # Rysuje symbole na ekranie (display_surface) dla każdego bębna
            self.reel_list[reel].symbol_list.update()  # Aktualizuje stan każdego symbolu na bębnie (np. animacje, pozycje)

