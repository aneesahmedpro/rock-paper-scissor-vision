#!/usr/bin/env python3

import os
import shutil
import pathlib

from camvision import CamVision
from gamedisplay import GameDisplay
from image_utils import save_binary_image


CAM_DEVICE_NUM = 0
BG_SAMPLES_COUNT = 30
CAPTURED_FRAMES_DIRNAME = 'captures'


def main():

    captured_frames_dir = pathlib.Path(CAPTURED_FRAMES_DIRNAME)

    if captured_frames_dir.exists():
        if captured_frames_dir.is_dir():
            if list(captured_frames_dir.iterdir()):
                cmd = input('There are some items in the "captures" '
                            'directory, proceeding will delete them all.\n'
                            'Proceed? (y/n): ')
                if cmd.lower() != 'y':
                    print('Quitting...')
                    return
            shutil.rmtree(str(captured_frames_dir))
        else:
            cmd = input('There is some file already present with the name '
                        '"captures", proceeding will delete it.\n'
                        'Proceed? (y/n): ')
            if cmd.lower() == 'y':
                captured_frames_dir.unlink()
            else:
                print('Quitting...')
                return

    captured_frames_dir.mkdir()

    camvision = CamVision(CAM_DEVICE_NUM)
    gamedisplay = GameDisplay()
    camvision.learn_bg_now(BG_SAMPLES_COUNT)
    num = 0

    os.chdir(str(captured_frames_dir))

    while True:
        camvision.capture_now()
        camvision.extract_fg()
        fg_mask = camvision.get_latest_fg_mask()
        fg_mask_img = fg_mask * 255
        gamedisplay.show_camvision_image(fg_mask_img)
        gamedisplay.show_repsonse_image('nothing')
        save_binary_image('{}.png'.format(num), fg_mask)
        num += 1
        if gamedisplay.check_quit_key_pressed():
            break

    print('Total', num, 'frames saved.')


if __name__ == '__main__':

    main()
