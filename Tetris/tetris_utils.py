import random


def map_to_pixel(x, y, tile_size=22):
    """Converteer map posities naar pixel posities

    Deze functie vergemakkelijkt het tekenen van het bord.
    """


class Board:
    def __init__(self, width, height):
        """Slaat breedte en hoogte van het bord op en maakt de datastructuur voor het bord in property "data"

        De property data bestaat uit een lijst van lijsten, met een lijst per rij van het
        tetris-bord. Iedere rij bevat net zoveel elementen als er kolommen zijn
        in het tetris bord.

        Een leeg vakje op het bord wordt voorgesteld door -1. Daarom wordt bij het
        aanmaken van de datastructuur ieder element op -1 gezet.
        """

    def out_of_left_border(self, player_x):
        """Controlleer dat positie player_x niet links van het bord ligt

        Geef True terug als player_x links van het bord ligt, anders False.
        """

    def out_of_top_border(self, player_y):
        """Controlleer dat positie player_y niet boven het bord ligt

        Geef True terug als player_y boven van het bord ligt, anders False.
        """

    def out_of_right_border(self, shape, player_x):
        """Controlleer dat de vorm shape op positie player_x niet rechtsbuiten het bord ligt"""

    def out_of_bottom_border(self, shape, player_y):
        """Controlleer dat de vorm shape op positie player_y niet onder het bord ligt"""

    def out_of_border(self, shape, player_x, player_y):
        """Controlleer dat de vorm shape op positie player_x, player_y niet buiten het bord ligt

        Gebruik hiervoor de eerder gemaakte out_of_left_border, out_of_top_border, out_of_right_border
        en out_of_bottom_border methods.

        Geef True terug als de shape buiten het bord ligt, anders False.
        """

    def check_collision(self, shape, player_x, player_y):
        """Controlleer of de vorm 'shape' op positie player_x, player_y overlapt met bestaande blokken.

        Controlleer eerst met de method out_of_border of je vorm binnen het bord ligt.
        Controlleer vervolgens of een blokje van je shape een vakje van het bord
        met een waarde groter dan -1 overlapt.

        Geef True terug als er een probleem is: M.a.w. als je out_of_border gaat,
        of als je een bestaande positie zou overschrijven.
        Geef in alle andere gevallen False terug.
        """

    def check_move_illegal(self, shape, player_x, player_y):
        """Controlleer of positie player_x player_y geldig is voor de huidige vorm 'shape'.

        Geef True terug als er een probleem is, anders False.
        """

    def copy_shape(self, shape, player_x, player_y, player_color):
        """Kopieer de vorm shape naar het bord op de opgegeven positie met de opgegeven kleur.

        Kopieer hiervoor voor iedere rij en iedere kolom van de vorm 'shape' de
        waarde van kleur naar het bord als de inhoud groter is dan 0.
        """

    def remove_full_rows(self):
        """Verwijder alle volle rijen en geef de verdiende punten score terug

        Als een volledige horizontale rij gevuld is, dient deze verwijderd te worden.
        In standaard Tetris krijg je hiervoor 100 punten. Geef daarom per verwijderde
        rij 100 punten terug.
        """


def random_block(shapes, colors, map_width):
    """Geef alle informatie over een nieuwe blok terug

    Deze functie geeft volgende informatie terug:
    - x positie
    - y positie
    - kleur
    - index in de vorm lijst (b.v. L-vormige blok)
    - index in de rotatie van die vorm
    """
    # Kies een vorm uit de lijst met vormen
    shape_idx = random.randint(0, len(shapes) - 1)
    # Om te debugging kan het interessant zijn, om telkens dezelfde
    # vorm te krijgen
    # shape_idx = 4

    shape = shapes[shape_idx]
    shape_rot = random.randint(0, len(shape) - 1)

    # Kies een kleur uit de lijst met kleuren
    color = random.randint(0, len(colors) - 1)
    # Om te debugging kan het interessant zijn, om telkens dezelfde
    # kleur aan een vorm toe te kennen (zo herken je de vorm dmv de kleur)
    # color = shape_idx

    # Plaats de blok in het midden van de eerste rij
    x = map_width // 2 - len(shape[shape_rot][0]) // 2
    y = 0
    return x, y, color, shape_idx, shape_rot


def detect_end(player_y):
    """Geef True terug als de blok de bovenkant van het bord raakt"""
    