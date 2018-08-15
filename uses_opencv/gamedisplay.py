import tkinter as tk

import numpy as np
import cv2

from config import CNN_INPUT_IMG_WIDTH, CNN_INPUT_IMG_HEIGHT


class GameDisplay:

    WIN_NAME_RESPONSE = 'reaction'
    WIN_NAME_CAMVISION = 'fg_mask'

    def __init__(self):

        # Load response images
        self.img_rock = cv2.imread('assets/rock.png')
        self.img_paper = cv2.imread('assets/paper.png')
        self.img_scissor = cv2.imread('assets/scissor.png')

        for img in [self.img_rock, self.img_paper, self.img_scissor]:
            if img is None:
                raise RuntimeError('Unable to find all image files for '
                                   'rock, paper, scissor')

        # Find screen dimensions
        root = tk.Tk()
        root.withdraw()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()

        # Calculate appropriate window positions (side-by-side arrangment)
        response_img_width, response_img_height = self.img_rock.shape[:2]
        both_win_combi_height = max(CNN_INPUT_IMG_HEIGHT, response_img_height)
        both_win_combi_width = CNN_INPUT_IMG_WIDTH + response_img_width
        win_camvision_x = (screen_width - both_win_combi_width) // 2
        win_camvision_y = (screen_height - both_win_combi_height) // 2
        win_response_x = win_camvision_x + 160
        win_response_y = win_camvision_y

        # Create windows at calculated positions
        cv2.namedWindow(GameDisplay.WIN_NAME_CAMVISION)
        cv2.namedWindow(GameDisplay.WIN_NAME_RESPONSE)
        cv2.moveWindow(
            GameDisplay.WIN_NAME_CAMVISION,
            win_camvision_x, win_camvision_y)
        cv2.moveWindow(
            GameDisplay.WIN_NAME_RESPONSE,
            win_response_x, win_response_y)

        # Create a 'black' image to show 'nothing'
        self.img_nothing = np.zeros((response_img_height, response_img_width))
        self.img_nothing = self.img_nothing.astype(np.uint8)

    def show_repsonse_image(self, posture):

        if posture == 'rock':
            cv2.imshow(GameDisplay.WIN_NAME_RESPONSE, self.img_rock)
        elif posture == 'paper':
            cv2.imshow(GameDisplay.WIN_NAME_RESPONSE, self.img_paper)
        elif posture == 'scissor':
            cv2.imshow(GameDisplay.WIN_NAME_RESPONSE, self.img_scissor)
        elif posture == 'nothing':
            cv2.imshow(GameDisplay.WIN_NAME_RESPONSE, self.img_nothing)

    def show_camvision_image(self, img):

        cv2.imshow(GameDisplay.WIN_NAME_CAMVISION, img)

    def check_quit_key_pressed(self):

        return (cv2.waitKey(1) & 0xFF) == 27  # Escape key

    def __del__(self):

        cv2.destroyAllWindows()
