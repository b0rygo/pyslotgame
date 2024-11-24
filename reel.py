from setting import *  # Importowanie ustawień gry (np. ścieżki do plików, symbole itp.)
import pygame, random  # Importowanie Pygame do zarządzania grafiką i Random do losowania symboli

class Reel:
    def __init__(self, pos):
        # Konstruktor klasy Reel, inicjalizuje pojedynczy bęben maszyny do gry
        self.symbol_list = pygame.sprite.Group()  # Tworzy grupę (kontener) do przechowywania symboli na bębnie
        self.shuffled_keys = list(symbols.keys())  # Pobiera listę nazw symboli ze słownika `symbols`
        random.shuffle(self.shuffled_keys)  # Tasuje kolejność symboli, aby były losowe
        self.shuffled_keys = self.shuffled_keys[:5]  # Wybiera pierwsze 5 symboli z przetasowanej listy

        self.reel_is_spinning = False  # Flaga określająca, czy bęben aktualnie się kręci

        # Tworzenie obiektów Symbol i ustawianie ich pozycji na bębnie
        for idx, item in enumerate(self.shuffled_keys):
            # Dodawanie nowego symbolu do listy symboli bębna
            self.symbol_list.add(Symbol(symbols[item], pos, idx))
            pos = list(pos)  # Zamiana pozycji na listę, aby można było ją zmodyfikować
            pos[1] += 300  # Przesunięcie pozycji pionowo o 300 pikseli (każdy symbol jest poniżej poprzedniego)
            pos = tuple(pos)  # Konwersja z powrotem do krotki (wymagane przez Pygame)

    def animate(self, delta_time):
        # Odpowiada za animowanie ruchu symboli na bębnie, kiedy bęben się kręci
        if self.reel_is_spinning:  # Sprawdzanie, czy bęben powinien się kręcić
            self.delay_time -= (delta_time * 1000)  # Zmniejszanie opóźnienia kręcenia
            self.spin_time -= (delta_time * 1000)  # Zmniejszanie całkowitego czasu kręcenia
            reel_is_stopping = False  # Flaga określająca, czy bęben ma się zatrzymać

            if self.spin_time < 0:  # Jeśli czas spinu minął
                reel_is_stopping = True  # Ustawienie flagi zatrzymania

            if self.delay_time <= 0:  # Jeśli minął czas opóźnienia
                for symbol in self.symbol_list:  # Przejście przez każdy symbol na bębnie
                    symbol.rect.bottom += 100  # Przesunięcie symbolu w dół o 100 pikseli

                    # Jeśli symbol przeszedł poza ekran
                    if symbol.rect.top == 1200:
                        if reel_is_stopping:  # Jeżeli bęben ma się zatrzymać
                            self.reel_is_spinning = False  # Wyłączenie kręcenia

                        symbol_idx = symbol.idx  # Pobranie indeksu symbolu
                        symbol.kill()  # Usunięcie symbolu, który wyszedł poza ekran
                        # Dodanie nowego symbolu na górze bębna z losowym symbolem
                        self.symbol_list.add(Symbol(symbols[random.choice(self.shuffled_keys)], (symbol.x_val, -300), symbol_idx))

    def start_spin(self, delay_time):
        # Rozpoczyna spin bębna z podanym opóźnieniem
        self.delay_time = delay_time  # Ustawia czas opóźnienia kręcenia
        self.spin_time = 1000 + delay_time  # Ustawia całkowity czas kręcenia (z opóźnieniem)
        self.reel_is_spinning = True  # Ustawia flagę, że bęben jest w ruchu

    def reel_spin_result(self):
        # Pobiera wynik spinu bębna jako listę symboli w odpowiedniej kolejności
        spin_symbols = []
        for i in GAME_INDICES:  # Iteruje przez indeksy symboli w widocznym obszarze
            symbol = self.symbol_list.sprites()[i].sym_type  # Pobiera typ symbolu dla danego indeksu
            spin_symbols.append(symbol)  # Dodaje symbol do listy wynikowej
        return spin_symbols[::-1]  # Odwraca kolejność, aby wyniki były zgodne z widokiem na ekranie

class Symbol(pygame.sprite.Sprite):
    # Klasa reprezentująca pojedynczy symbol na bębnie
    def __init__(self, pathToFile, pos, idx):
        super().__init__()  # Inicjalizacja klasy bazowej (pygame.sprite.Sprite)

        # Pobieranie typu symbolu na podstawie nazwy pliku
        self.sym_type = pathToFile.split('/')[-1].split('.')[0]  # Wyciąga nazwę pliku i usuwa rozszerzenie

        self.pos = pos  # Ustawia pozycję symbolu na ekranie
        self.idx = idx  # Indeks symbolu (jego kolejność na bębnie)
        self.image = pygame.image.load(pathToFile).convert_alpha()  # Wczytuje obraz symbolu i konwertuje z obsługą przezroczystości
        self.rect = self.image.get_rect(topleft=pos)  # Tworzy prostokąt (rect) opisujący pozycję symbolu
        self.x_val = self.rect.left  # Przechowuje współrzędną x lewego boku symbolu

    def update(self):
        pass
