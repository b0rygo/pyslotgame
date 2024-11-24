from setting import *  # Importowanie ustawień gry (np. parametrów gracza, jeśli są zdefiniowane w module `setting`)

class Player:
    def __init__(self):
        # Konstruktor klasy Player, inicjalizuje parametry gracza
        self.balance = 1000.00  # Początkowy balans gracza
        self.bet_size = 10.00  # Domyślna wartość zakładu
        self.last_payout = 0.00  # Ostatnia wygrana gracza (na początku brak wygranej)
        self.total_won = 0.00  # Całkowita kwota wygranych
        self.total_wager = 0.00  # Całkowita kwota obstawionych zakładów

    def get_data(self):
        # Pobiera aktualne dane gracza w formacie słownika z zaokrągleniem wartości do dwóch miejsc po przecinku
        player_data = {}  # Tworzenie pustego słownika na dane gracza
        player_data['balance'] = "{:.2f}".format(self.balance)  # Formatowanie balansu gracza jako string z 2 miejscami dziesiętnymi
        player_data['bet_size'] = "{:.2f}".format(self.bet_size)  # Formatowanie wartości zakładu
        player_data['last_payout'] = "{:.2f}".format(self.last_payout) if self.last_payout else "0.00"  # Formatowanie ostatniej wygranej lub "0.00", jeśli brak wygranej
        player_data['total_won'] = "{:.2f}".format(self.total_won)  # Formatowanie całkowitych wygranych
        player_data['total_wager'] = "{:.2f}".format(self.total_wager)  # Formatowanie całkowitych zakładów
        return player_data  # Zwracanie słownika z danymi gracza

    def place_bet(self):
        # Funkcja odpowiadająca za obstawianie zakładu
        bet = self.bet_size  # Pobranie wartości zakładu
        self.balance -= bet  # Zmniejszenie balansu gracza o wartość zakładu
        self.total_wager += bet  # Dodanie wartości zakładu do całkowitej kwoty obstawionej
