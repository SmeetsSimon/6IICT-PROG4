import pygame

pygame.init()

# Klasse als container voor de kleuren
class Kleur:
    # Bewaar in deze klasse volgende kleuren via een lijst met RGB'waarden:
    # Zwart, wit, groen, rood, grijs
    # 
    # Maak ook een "gradient" variabele aan, 
    # dit is een lijst die bestaat uit drie kleuren grijs:
    # [127, 127, 127], [160, 160, 160], [192, 192, 192] 
    ZWART = (0,0,0)
    WIT = (255,255,255)
    GROEN = (0,255,0)
    ROOD = (255,0,0)
    GRADIENT = [(128,128,128), (211,211,211), (192,192,192)]

    

# Klasse om de fonts bij te houden
class Fonts:
    # Maak twee fonts aan MBV pygame:
    # FONT_NORMAAL: met lettertype arial en grootte 30
    # FONT_GROOT: met lettertype arial en grootte 60
    FONT_NORMAAL = pygame.font.SysFont("arial.ttf",30)
    FONT_GROOT = pygame.font.SysFont("arial.ttf",60)
    
