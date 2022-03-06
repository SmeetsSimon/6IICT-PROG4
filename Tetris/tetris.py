import pygame

from tetris_utils import Board, detect_end, map_to_pixel, random_block
from tetris_colors import COLORS
from tetris_shapes import shapes

WIDTH = 800
HEIGHT = 600
COLOR = 45
MAP_WIDTH = 10
MAP_HEIGHT = 20
screen = None


class PygameBoard(Board):
    def draw(self):
        """Teken het hele bord rij voor rij"""
        # TODO

    def draw_shape(
        self,
        shape,
        player_x,
        player_y,
        player_color,
    ):
        """Teken de huidige vorm op de correcte positie"""
        # TODO


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Maak een bord aan met een bepaalde hoogte en breedte
board = PygameBoard(MAP_WIDTH, MAP_HEIGHT)

# Kies de initiele random blok
player_x, player_y, player_color, player_shape, player_shape_rot = random_block(
    shapes, COLORS, MAP_WIDTH
)

running = True
while running:
    # Haal de gekozen vorm op uit de lijst met vormen (b.v. de L vorm)
    # Je krijgt dan een lijst met alle rotaties van die vorm
    all_rotated_shapes = shapes[player_shape]

    # Haal de gekozen rotatie op van de gekozen vorm
    shape = all_rotated_shapes[player_shape_rot]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Als het mag, verplaats dan de positie van het blok 1 naar onder
                # TODO
                pass

            if event.key == pygame.K_LEFT:
                # Als het mag, verplaats dan de positie van het blok 1 naar links
                # TODO
                pass

            if event.key == pygame.K_RIGHT:
                # Als het mag, verplaats dan de positie van het blok 1 naar rechts
                # TODO
                pass

            if event.key == pygame.K_UP:
                # Als het mag roteer dan de huidige blok
                max_rots = len(shapes[player_shape])
                new_player_shape_rot = player_shape_rot + 1
                new_player_shape_rot = new_player_shape_rot % max_rots
                new_shape = shapes[player_shape][new_player_shape_rot]
                if not board.check_move_illegal(new_shape, player_x, player_y):
                    shape = new_shape
                    player_shape_rot = new_player_shape_rot
                else:
                    print(
                        "out of bounds",
                        player_x,
                        player_y,
                        player_shape_rot,
                        shape,
                        new_shape,
                    )

    # Maak het scherm leeg
    screen.fill("black")

    # Teken het bord met de reeds geplaatste blokken
    board.draw()

    # Teken de huidige blok
    board.draw_shape(
        shape,
        player_x,
        player_y,
        player_color,
    )

    pygame.display.flip()

    # Wacht
    clock.tick(5)

    # Controlleer of er een botsing is met een bestaande blok als de blok 1 positie
    # naar onder zou vallen
    if board.check_collision(shape, player_x, player_y + 1):
        # Controlleer of het spel gedaan is
        if detect_end(player_y):
            print("the end")
            break

        # Als er een botsing is met een bestaande blok, kopieer de huidige
        # blok dan naar het bord
        board.copy_shape(shape, player_x, player_y, player_color)
        (
            player_x,
            player_y,
            player_color,
            player_shape,
            player_shape_rot,
        ) = random_block(shapes, COLORS, MAP_WIDTH)

    # Verplaats de blok 1 positie naar onder
    player_y += 1

    # Verwijder volle rijen
    board.remove_full_rows()