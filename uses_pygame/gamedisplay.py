import numpy as np
import pygame

from config import CNN_INPUT_IMG_WIDTH, CNN_INPUT_IMG_HEIGHT
from image_utils import surface_from_array


class GameDisplay:

    def __init__(self):

        self.img_rock = pygame.image.load('assets/rock.png')
        self.img_paper = pygame.image.load('assets/paper.png')
        self.img_scissor = pygame.image.load('assets/scissor.png')

        self.rect_camvision_img = pygame.Rect(
            (0, 0, CNN_INPUT_IMG_WIDTH, CNN_INPUT_IMG_HEIGHT))
        self.rect_response_img = self.img_rock.get_rect().move(
            self.rect_camvision_img.width, 0)
        self.rect_display = self.rect_camvision_img.union(
            self.rect_response_img)

        self.display_surface = pygame.display.set_mode(
            (self.rect_display.width, self.rect_display.height))

        self.img_rock = self.img_rock.convert()
        self.img_paper = self.img_paper.convert()
        self.img_scissor = self.img_scissor.convert()

        arr = np.zeros((self.img_rock.get_width(), self.img_rock.get_height()))
        arr = arr.astype(np.uint8)
        self.img_nothing = pygame.surfarray.make_surface(arr)

    def show_repsonse_image(self, posture):

        if posture == 'rock':
            self.display_surface.blit(self.img_rock, self.rect_response_img)
        elif posture == 'paper':
            self.display_surface.blit(self.img_paper, self.rect_response_img)
        elif posture == 'scissor':
            self.display_surface.blit(self.img_scissor, self.rect_response_img)
        elif posture == 'nothing':
            self.display_surface.blit(self.img_nothing, self.rect_response_img)

        pygame.display.update(self.rect_response_img)

    def show_camvision_image(self, image_array):

        surface = surface_from_array(image_array)
        self.display_surface.blit(surface, self.rect_camvision_img)
        pygame.display.update(self.rect_camvision_img)

    def check_quit_key_pressed(self):

        events = pygame.event.get()

        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return True

        return False

    def __del__(self):

        pass
