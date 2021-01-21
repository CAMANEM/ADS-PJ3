import pygame, os
from Graphics.imagenes import Imagen
from Graphics.TextBox import InputBox
from Graph_Logic.graph import Graph

pygame.init()
size = (900, 800)
black = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
images_list = pygame.sprite.Group()
image_selected = False
running = True

saved_coord = None
saved_id = None

grafo = Graph()
lines = grafo.get_connections()

resistor = pygame.image.load(os.getcwd() + "\\Graphics\\images\\resistor.png").convert_alpha()
resistor_boolean = False
cell = pygame.image.load(os.getcwd() + "\\Graphics\\images\\cell.png").convert_alpha()
cell_boolean = False
check = pygame.image.load(os.getcwd() + "\\Graphics\\images\\check.png").convert_alpha()

line_selected = False

input_box = InputBox(600, 730, 150, 40)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if y > 700:
                if 50 < x < 110 and 720 < y < 780:
                    cell_boolean = True
                    resistor_boolean = False
                    line_selected = False
                    # for imagen in images_list:
                    #     imagen.clear()
                elif 200 < x < 260 and 720 < y < 780:
                    cell_boolean = False
                    resistor_boolean = True
                    line_selected = False
                    # for imagen in images_list:
                    #     imagen.clear()
                elif 350 < x < 410 and 220 < y < 780:
                    cell_boolean = False
                    resistor_boolean = False
                    line_selected = True
                    # for imagen in images_list:
                    #     imagen.clear()

            if line_selected:
                for imagen in images_list:
                    if imagen.rect.collidepoint(pos):
                        result = imagen.check_side()
                        if result == -1:
                            print("ya seleccionado")
                        elif saved_coord == None:
                            saved_coord = result
                            saved_id = imagen.id
                        else:
                            grafo.add_edge(saved_id, imagen.id, int(input_box.text), saved_coord, result)
                            lines = grafo.get_connections()
                            saved_coord = None
                            saved_id = None
                            print(lines)



            else:
                if x < 860 and y < 660 and event.button == 3:
                    if cell_boolean:
                        images_list.add(Imagen(x, y, "cell.png", int(input_box.text)))
                        grafo.add_apex(int(input_box.text), x, y)
                    elif resistor_boolean:
                        images_list.add(Imagen(x, y, "resistor.png", int(input_box.text)))
                        grafo.add_apex(int(input_box.text), x, y)
                    else:
                        pass
                elif event.button == 1 and image_selected == False:
                    for imagen in images_list:
                        if imagen.rect.collidepoint(pos):
                            image_selected = True
                            imagen.clicked = True
                            break


        if event.type == pygame.MOUSEBUTTONUP:
            image_selected = False
            for imagen in images_list:
                imagen.clicked = False

        input_box.handle_event(event)
        input_box.update()
        # Logica aqui

    for imagen in images_list:
        if imagen.clicked:
            pos = pygame.mouse.get_pos()
            if 25 < pos[0] < 880 and 25 < pos[1] < 680:
                grafo.apex[imagen.id].x = pos[0] - (imagen.rect.width / 2)
                grafo.apex[imagen.id].y = pos[1] - (imagen.rect.width / 2)
                imagen.rect.x = pos[0] - (imagen.rect.width / 2)
                imagen.rect.y = pos[1] - (imagen.rect.width / 2)

    screen.fill(white)

    for i in lines:
        fix_x1 = 0
        fix_x2 = 0

        for j in grafo.apex[i[0]].neighbor:
            if j[2] == 1:
                fix_x1 = 59

        for l in grafo.apex[i[0]].neighbor:
            if l[3] == 1:
                fix_x2 = 59

        x_line1 = grafo.apex[i[0]].x + fix_x1
        y_line1 = grafo.apex[i[0]].y + 27.5
        x_line2 = grafo.apex[i[1]].x + fix_x2
        y_line2 = grafo.apex[i[1]].y + 27.5

        pygame.draw.line(screen, black, (x_line1, y_line1), (x_line2, y_line2), 3)


    screen.blit(cell, (50, 720))
    screen.blit(resistor, (200, 720))
    input_box.draw(screen)

    if cell_boolean:
        screen.blit(check, (120,737))
    elif resistor_boolean:
        screen.blit(check, (270,737))
    elif line_selected:
        screen.blit(check, (420, 737))


    pygame.draw.line(screen, black, (0, 700), (900, 700), 5)
    pygame.draw.line(screen, black, (350, 750), (410, 750), 4)

    images_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
