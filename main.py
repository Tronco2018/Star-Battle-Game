import pygame
import random

pygame.init()

lar = 800
alt = 365

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 50, 50)
blue = (0, 0, 250)
green = (0, 100, 0)

punteggio = 0
font = pygame.font.SysFont("Calibri", 60, bold=True, italic=False)

larghezza_example = 50
altezza_example = 50
speed_example = 1



larghezza_palla = 20
altezza_palla = 20
velocita_palla_x = 1
velocita_palla_y = 0

larghezza_palla2 = 20
altezza_palla2 = 20
velocita_palla2_x = 1
velocita_palla2_y = 0

palla = pygame.Rect(799 - larghezza_palla,
                    250,
                    larghezza_palla, altezza_palla)

palla2 = pygame.Rect(800 + larghezza_palla2,
                    190,
                    larghezza_palla2, altezza_palla2)


example = pygame.Rect(50 - larghezza_example, 
                      300,
                      larghezza_example, altezza_example)



# caricamento e posizionamento navicella
navicella = pygame.image.load("navicella.png")
navicella_rect = navicella.get_rect()
navicella_rect.move_ip(100, 200)
navicella = pygame.transform.scale(navicella, (50, 50))

meteorite = pygame.image.load("meteorite.png")
meteorite_rect = meteorite.get_rect()
meteorite_rect.move_ip(100, 200)
meteorite = pygame.transform.scale(meteorite, (30, 20))

finestra = pygame.display.set_mode((lar, alt))
pygame.display.set_caption("Star fighter")

def draw():
    finestra.fill(black)
    finestra.blit(navicella, example) # disegno navicella sopra il rettangolo example
    finestra.blit(meteorite, palla)
    finestra.blit(meteorite, palla2)
    testo = font.render(str(punteggio), True, white)
    finestra.blit(testo, (lar // 2 - testo.get_width() // 2, alt // 2 - testo.get_height() // 2 + 100)) 



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    draw()

    

    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_UP]:
        example.y -= speed_example
    
    if tasti[pygame.K_DOWN]:
         example.y += speed_example

    if tasti[pygame.K_LEFT]:
        example.x -= speed_example
    
    if tasti[pygame.K_RIGHT]:
        example.x += speed_example



    if example.top <= 0 :
        example.y += 1
    
    if example.left <= 0 :
        example.x += 1
    
    if example.right >= 800 :
        example.x -= 1

    if tasti[pygame.K_1]:
        velocita_palla_x == 1

    if tasti[pygame.K_2]:
        velocita_palla_x == 2



    if example.bottom >= 367:
        example.y -= 3

    if palla.top <= 0 :
        pygame.quit()
        print("Unespected error error number:(2)")
        quit()
    

    if palla.right >= 800 :
        pygame.quit()
        print("Unespected error error number:(3)")
        quit()

    if palla.left <= 0:
        palla.x += 799 - larghezza_palla
        palla.y = random.randint(50, 290)
        punteggio += 1

    if velocita_palla_x == 2:
        palla.x -= 3

    if velocita_palla_x == 1:
        palla.x -= 1
    

    
    if palla.colliderect(example):
        pygame.quit()
        print("Game over! Il tuo punteggio è:" + "" + str(punteggio))
        quit()

    pygame.display.update()

    if tasti[pygame.K_1]:
        velocita_palla2_x == 1

    if tasti[pygame.K_2]:
        velocita_palla2_x == 2



    if palla2.top <= 0 :
        pygame.quit()
        print("Unespected error error number:(2)")
        quit()
    



    if palla2.left <= 0:
        palla2.x += 799 - larghezza_palla2
        palla2.y = random.randint(50, 290)
        punteggio += 1


    if punteggio >= 10:
           
        
        


        if velocita_palla2_x == 1:
            palla2.x -= 1.5
    

    
        if palla2.colliderect(example):
            pygame.quit()
            print("Game over! Il tuo punteggio è:" + "" + str(punteggio))
            quit()
