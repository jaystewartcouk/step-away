import pygame


class Window:
    def open(text):
        pygame.init()
        screen_size = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 32)
        text_surface = font.render(text, True, (255, 255, 255))
        # get the dimensions of the text surface
        text_width, text_height = text_surface.get_size()
        # calculate the center position for the text
        x = (screen_size[0] / 2) - (text_width / 2)
        y = (screen_size[1] / 2) - (text_height / 2)
        # blit the text surface onto the center of the screen
        screen.blit(text_surface, (x, y))
        # update the display
        pygame.display.flip()

    def close():
        pygame.quit()
