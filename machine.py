from player import Player
from reel import *
from setting import *
from win import *
import pygame

class Machine:
    def __init__(self):
        # Inicjalizacja ustawień maszyny do gry
        self.display_surface = pygame.display.get_surface()  # Pobranie bieżącej powierzchni wyświetlania Pygame
        self.machine_balance = 10000.00  # Początkowy balans maszyny
        self.reel_index = 0  # Indeks do śledzenia bębnów
        self.reel_list = {}  # Słownik przechowujący wszystkie bębny
        self.can_toggle = True  # Flaga pozwalająca na przełączanie między spinem a zatrzymaniem bębnów
        self.spinning = False  # Informacja, czy bębny są obecnie w ruchu
        self.can_animate = False  # Flaga pozwalająca na uruchomienie animacji
        self.win_animation_ongoing = False  # Informacja, czy trwa animacja wygranej

        # Wyniki z obrotów bębnów (poprzednie i bieżące)
        self.prev_result = {0: None, 1: None, 2: None, 3: None, 4: None}  # Wyniki z poprzedniego obrotu
        self.spin_result = {0: None, 1: None, 2: None, 3: None, 4: None}  # Wyniki z bieżącego obrotu

        self.spawn_reels()  # Tworzenie bębnów
        self.currPlayer = Player()  # Inicjalizacja gracza

    def cooldowns(self):
        # Sprawdzanie, czy wszystkie bębny są zatrzymane i można rozpocząć nowy obrót
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:  # Jeżeli którykolwiek z bębnów się kręci
                self.can_toggle = False  # Nie można przełączyć na nowy spin
                self.spinning = True  # Maszyna jest w trybie spinowania

        # Sprawdzanie, czy wszystkie bębny są zatrzymane
        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True  # Można ponownie uruchomić spin
            self.spin_result = self.get_result()  # Pobieranie wyników z bębnów

            # Sprawdzanie, czy nastąpiła wygrana
            if self.check_wins(self.spin_result):
                self.win_data = self.check_wins(self.spin_result)  # Dane dotyczące wygranej
                # Odtwarzanie dźwięku wygranej (dźwięk należy dodać)
                # self.play_win_sound(self.win_data)
                self.pay_player(self.win_data, self.currPlayer)  # Wypłata nagrody graczowi
                # self.win_animation_ongoing = True  # Flaga animacji wygranej
                print(self.currPlayer.get_data())  # Debugowanie: wyświetlanie danych gracza

    def input(self):
        # Obsługa wejścia klawiatury przez gracza
        keys = pygame.key.get_pressed()  # Sprawdzanie naciśniętych klawiszy

        # Sprawdzanie, czy gracz nacisnął SPACJĘ, może wykonać spin i ma wystarczające środki
        if keys[pygame.K_SPACE] and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
            self.toggle_spinning()  # Rozpoczęcie obrotu bębnów
            self.spin_time = pygame.time.get_ticks()  # Rejestrowanie czasu rozpoczęcia spinu
            self.currPlayer.place_bet()  # Pobranie zakładu od gracza
            self.machine_balance += self.currPlayer.bet_size  # Dodanie zakładu do balansu maszyny
            self.currPlayer.last_payout = None  # Zerowanie ostatniej wygranej
            print(self.currPlayer.get_data())  # Debugowanie: wyświetlanie danych gracza

    def draw_reels(self, delta_time):
        # Rysowanie bębnów na ekranie
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)  # Animacja bębnów

    def spawn_reels(self):
        # Tworzenie bębnów i ustawianie ich pozycji
        if not self.reel_list:
            x_topleft, y_topleft = 10, -300  # Pozycja pierwszego bębna
        while self.reel_index < 5:  # Tworzenie 5 bębnów
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (300 + X_OFFSET), y_topleft  # Ustawianie pozycji kolejnych bębnów

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))  # Dodanie bębna do listy
            self.reel_index += 1  # Przesunięcie indeksu

    def toggle_spinning(self):
        # Przełączanie między spinem a zatrzymaniem bębnów
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()  # Rejestrowanie czasu rozpoczęcia
            self.spinning = not self.spinning  # Zmiana stanu spinu
            self.can_toggle = False  # Blokada do czasu zakończenia spinu

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)  # Uruchomienie spinu bębna z opóźnieniem
                # self.spin_sound.play()  # Odtwarzanie dźwięku spinu (dźwięk należy dodać)
                self.win_animation_ongoing = False  # Zatrzymanie animacji wygranej

    def get_result(self):
        # Pobieranie wyników spinu z bębnów
        for reel in self.reel_list:
            spin_result = self.reel_list[reel].reel_spin_result()  # Wynik spinu dla danego bębna

            # Sprawdzanie, czy symbole są prawidłowe i przypisane do grafiki
            self.spin_result[reel] = []
            for sym in spin_result:
                if sym in symbols:
                    self.spin_result[reel].append(symbols[sym])  # Dodanie ścieżki grafiki do wyniku

        return self.spin_result  # Zwrócenie wyników spinu

    def check_wins(self, result):
        # Sprawdzanie, czy wystąpiła wygrana
        hits = {}  # Słownik przechowujący dane o wygranych
        horizontal = flip_horizontal(result)  # Transponowanie wyników do wierszy

        for row in horizontal:
            for sym in row:
                if row.count(sym) > 2:  # Jeżeli dany symbol występuje więcej niż 2 razy
                    possible_win = [idx for idx, val in enumerate(row) if sym == val]  # Indeksy zwycięskich symboli

                    # Sprawdzanie, czy występuje sekwencja wygranej
                    if len(longest_seq(possible_win)) > 2:
                        hits[horizontal.index(row) + 1] = [sym, longest_seq(possible_win)]  # Dodanie do wygranych
        if hits:
            self.can_animate = True  # Flaga pozwalająca na animację wygranej
            return hits  # Zwrócenie wygranych danych

    def pay_player(self, win_data, curr_player):
        # Wypłata wygranej graczowi
        multiplier = 0  # Mnożnik wygranej
        spin_payout = 0  # Kwota wygranej

        for v in win_data.values():
            multiplier += len(v)  # Dodanie liczby wygranych symboli
            print(v)  # Debugowanie: Wyświetlenie wygranych danych

        spin_payout = (multiplier * curr_player.bet_size)  # Obliczanie wypłaty
        curr_player.balance += spin_payout  # Dodanie wygranej do balansu gracza
        self.machine_balance -= spin_payout  # Odjęcie wygranej z balansu maszyny
        curr_player.last_payout = spin_payout  # Zapisanie ostatniej wygranej
        curr_player.total_won += spin_payout  # Aktualizacja całkowitych wygranych gracza

    def update(self, delta_time):
        # Główna funkcja aktualizująca stan maszyny
        self.cooldowns()  # Sprawdzanie stanu bębnów
        self.input()  # Obsługa wejścia
        self.draw_reels(delta_time)  # Rysowanie bębnów

        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)  # Rysowanie symboli na bębnach
            self.reel_list[reel].symbol_list.update()  # Aktualizacja symboli

# Balance/payout debugger
        # debug_player_data = self.currPlayer.get_data()
        # machine_balance = "{:.2f}".format(self.machine_balance)
        # if self.currPlayer.last_payout:
        #     last_payout = "{:.2f}".format(self.currPlayer.last_payout)
        # else:
        #     last_payout = "N/A"
        # debug(f"Player balance: {debug_player_data['balance']} | Machine balance: {machine_balance} | Last payout: {last_payout}")