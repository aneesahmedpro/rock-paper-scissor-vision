import numpy as np
import pygame


def array_from_surface(surface):

    image_array = pygame.surfarray.array3d(surface).swapaxes(0, 1)
    return image_array


def surface_from_array(image_array):

    surface = pygame.surfarray.make_surface(image_array.swapaxes(0, 1))
    return surface


def load_binary_image(filename):

    img = pygame.image.load(filename)
    img = array_from_surface(img)
    img = img[:, :, 0]
    img = img // 255

    return img


def save_binary_image(filename, img):

    img = img * 255
    img = np.atleast_3d(img)
    img = np.repeat(img, 3, axis=2)
    surface = surface_from_array(img)
    pygame.image.save(surface, filename)
