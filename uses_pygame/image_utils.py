import numpy as np
import pygame


def load_binary_image(filename):

    img = pygame.image.load(filename)
    img = pygame.surfarray.array3d(img).swapaxes(0, 1)
    img = img[:, :, 0]
    img = img // 255

    return img


def save_binary_image(filename, img):

    img = img * 255
    img = np.atleast_3d(img)
    img = np.repeat(img, 3, axis=2)
    surface = pygame.surfarray.make_surface(img.swapaxes(0, 1))
    pygame.image.save(surface, filename)
