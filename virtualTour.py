import pygame

# initialize pygame
pygame.init()

# set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load the campus map image
campus_map = pygame.image.load("coe.jpg").convert()

# set the starting position of the virtual tour
position_x = 0
position_y = 0

# set the speed of movement
speed = 5

# set the zoom level
zoom = 1.0

# set the main loop flag
running = True

# set the clock for slow motion effect
clock = pygame.time.Clock()
fps = 30

# set the slow motion factor
slow_motion_factor = 5

# create font object
font = pygame.font.Font(None, 36)

# create zoom in button
zoom_in_button = pygame.Rect(SCREEN_WIDTH - 80, 20, 60, 40)
zoom_in_text = font.render("+", True, (0, 0, 0))

# create zoom out button
zoom_out_button = pygame.Rect(SCREEN_WIDTH - 80, 80, 60, 40)
zoom_out_text = font.render("-", True, (0, 0, 0))

# set the drag and move flag
dragging = False

# set the previous position of the mouse
previous_mouse_pos = None

# main loop
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # check if zoom in button is clicked
                if zoom_in_button.collidepoint(event.pos):
                    zoom += 0.1
                # check if zoom out button is clicked
                elif zoom_out_button.collidepoint(event.pos):
                    zoom -= 0.1
                    zoom = max(0.1, zoom)
                # check if mouse is clicked on the image
                elif campus_map.get_rect().move(position_x, position_y).collidepoint(event.pos):
                    dragging = True
                    previous_mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:

            # move the image if dragging is True and within the image boundaries
            if dragging:
                mouse_pos = event.pos
                delta_x = mouse_pos[0] - previous_mouse_pos[0]
                delta_y = mouse_pos[1] - previous_mouse_pos[1]
                new_pos_x = position_x + delta_x
                new_pos_y = position_y + delta_y
                image_rect = campus_map.get_rect().move(new_pos_x, new_pos_y)
                if image_rect.left <= 0 and image_rect.right >= SCREEN_WIDTH:
                    position_x = new_pos_x
                if image_rect.top <= 0 and image_rect.bottom >= SCREEN_HEIGHT:
                    position_y = new_pos_y
                previous_mouse_pos = mouse_pos
    
    # get the pressed keys
    keys = pygame.key.get_pressed()
    
    # move the position based on the pressed keys
    if keys[pygame.K_LEFT]:
        position_x += speed
    if keys[pygame.K_RIGHT]:
        position_x -= speed
    if keys[pygame.K_UP]:
        position_y += speed
    if keys[pygame.K_DOWN]:
        position_y -= speed
    
    # clear the screen
    screen.fill((255, 255, 255))

    # scale the campus map image based on the zoom level
    scaled_campus_map = pygame.transform.scale(campus_map, (int(campus_map.get_width() * zoom), int(campus_map.get_height() * zoom)))

    # get the rectangle of the scaled campus map
    scaled_campus_map_rect = scaled_campus_map.get_rect()

    # adjust the position of the campus map to prevent it from moving out of the screen
    if position_x > 0:
        position_x = 0
    elif position_x < SCREEN_WIDTH - scaled_campus_map_rect.width:
        position_x = SCREEN_WIDTH - scaled_campus_map_rect.width

    if position_y > 0:
        position_y = 0
    elif position_y < SCREEN_HEIGHT - scaled_campus_map_rect.height:
        position_y = SCREEN_HEIGHT - scaled_campus_map_rect.height

        # get the rectangle of the scaled campus map
        scaled_campus_map_rect = scaled_campus_map.get_rect()

        # adjust the position of the campus map to prevent it from moving out of the screen
        if position_x > 0:
            position_x = 0
        elif position_x < SCREEN_WIDTH - scaled_campus_map_rect.width:
                position_x = SCREEN_WIDTH - scaled_campus_map_rect.width
                if position_y > 0:
                    position_y = 0
                elif position_y < SCREEN_HEIGHT - scaled_campus_map_rect.height:
                    position_y = SCREEN_HEIGHT - scaled_campus_map_rect.height

    # draw the campus map image
    screen.blit(scaled_campus_map, (position_x, position_y))

    # draw the zoom in button
    pygame.draw.rect(screen, (255, 255, 255), zoom_in_button)
    pygame.draw.rect(screen, (0, 0, 0), zoom_in_button, 2)
    screen.blit(zoom_in_text, (SCREEN_WIDTH - 60, 30))

    # draw the zoom out button
    pygame.draw.rect(screen, (255, 255, 255), zoom_out_button)
    pygame.draw.rect(screen, (0, 0, 0), zoom_out_button, 2)
    screen.blit(zoom_out_text, (SCREEN_WIDTH - 60, 90))

    # update the display
    pygame.display.flip()

    # limit the frame rate for slow motion effect
    clock.tick(fps // slow_motion_factor)

# quit pygame
pygame.quit()
