#!/usr/bin/env python3

from camvision import CamVision
from gamedisplay import GameDisplay


CAM_DEVICE_NUM = 0
BG_SAMPLES_COUNT = 30


def main():

    camvision = CamVision(CAM_DEVICE_NUM)
    gamedisplay = GameDisplay()
    camvision.learn_bg_now(BG_SAMPLES_COUNT)

    while True:
        camvision.capture_now()
        camvision.extract_fg()
        fg_mask_img = camvision.get_latest_fg_mask() * 255
        gamedisplay.show_camvision_image(fg_mask_img)
        gamedisplay.show_repsonse_image('nothing')
        if gamedisplay.check_quit_key_pressed():
            break


if __name__ == '__main__':

    main()
