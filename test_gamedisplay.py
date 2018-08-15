#!/usr/bin/env python3

import itertools
import time

import numpy as np

from config import CNN_INPUT_IMG_WIDTH, CNN_INPUT_IMG_HEIGHT
from gamedisplay import GameDisplay


def main():

    img_array = np.zeros((CNN_INPUT_IMG_HEIGHT, CNN_INPUT_IMG_WIDTH))
    img_array = img_array.astype(np.uint8)
    col = CNN_INPUT_IMG_WIDTH // 2
    img_array[:, col:] = 255
    postures = ['rock', 'paper', 'scissor', 'nothing']
    gamedisplay = GameDisplay()
    start_time = 0
    posture_generator = itertools.cycle(postures)

    while True:
        if (time.time() - start_time) > 0.5:
            posture = next(posture_generator)
            start_time = time.time()

        gamedisplay.show_repsonse_image(posture)
        gamedisplay.show_camvision_image(img_array)
        if gamedisplay.check_quit_key_pressed():
            break

        time.sleep(0.1)


if __name__ == '__main__':

    main()
