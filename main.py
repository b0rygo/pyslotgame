from machine import Machine
from setting import *
from reel import *
import ctypes, pygame, sys

# Ustawienia rozdzielczości niezależnie od ustawień skalowania w systemie Windows
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):
        # Ogólna konfiguracja gry
        pygame.init()  # Inicjalizacja Pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Tworzenie okna gry o określonych wymiarach
        pygame.display.set_caption('Slot Machine Demo')  # Ustawianie tytułu okna
        self.clock = pygame.time.Clock()  # Utworzenie zegara Pygame do kontrolowania FPS
        self.machine = Machine()  # Inicjalizacja maszyny (slot machine)
        self.delta_time = 0  # Zmienna do śledzenia czasu między klatkami
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)  # Wczytanie tła gry z pliku

    def run(self):
        # Główna pętla gry
        self.start_time = pygame.time.get_ticks()  # Pobranie czasu rozpoczęcia pętli w milisekundach

        while True:
            # Obsługa zdarzeń (np. zamknięcie okna)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Sprawdzenie, czy użytkownik chce zamknąć okno
                    pygame.quit()  # Zamykanie Pygame
                    sys.exit()  # Zakończenie programu

            # Obliczanie delta_time (czasu między klatkami) w sekundach
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000  # Czas od ostatniego odświeżenia
            self.start_time = pygame.time.get_ticks()  # Aktualizacja czasu rozpoczęcia

            # Aktualizacja ekranu
            pygame.display.update()  # Aktualizacja całego ekranu gry
            self.screen.blit(self.bg_image, (0, 0))  # Rysowanie tła na ekranie
            self.machine.update(self.delta_time)  # Aktualizacja logiki maszyny (slot machine)
            self.clock.tick(FPS)  # Utrzymywanie stałej liczby klatek na sekundę

if __name__ == '__main__':
    # Uruchamianie gry
    game = Game()  # Tworzenie instancji klasy `Game`
    game.run()  # Wywołanie metody `run`, która rozpoczyna główną pętlę gry
