import numpy as np
import pygame
import pygame.camera

from config import CAMVISION_IMG_WIDTH, CAMVISION_IMG_HEIGHT


class CamVision:

    def __init__(self, cam_device_num):

        pygame.camera.init()
        cam_device = pygame.camera.list_cameras()[cam_device_num]
        self.cam = pygame.camera.Camera(
            cam_device,
            (CAMVISION_IMG_WIDTH, CAMVISION_IMG_HEIGHT))
        self.cam.start()
        self.cam_surface = pygame.surface.Surface(
            (CAMVISION_IMG_WIDTH, CAMVISION_IMG_HEIGHT))
        self.learned_bg = None
        self.latest_frame = None
        self.latest_fg_mask = None

    def capture_now(self):

        self.cam.get_image(self.cam_surface)
        array_img = pygame.surfarray.array3d(self.cam_surface).swapaxes(0, 1)
        self.latest_frame = array_img

    def learn_bg_now(self, img_samples_count):

        bg_samples = []
        for i in range(img_samples_count):
            self.capture_now()
            bg_samples.append(self.latest_frame)
        bg_samples = np.array(bg_samples)
        self.learned_bg = np.mean(bg_samples, axis=0)

    def extract_fg(self):

        diff = self.latest_frame - self.learned_bg
        distance = np.sqrt(np.sum(np.square(diff), axis=2))
        fg_mask = distance > 32
        self.latest_fg_mask = fg_mask.astype(np.uint8)

    def get_latest_frame(self):

        return self.latest_frame

    def get_latest_fg_mask(self):

        return self.latest_fg_mask

    def get_learned_bg(self):

        return self.learned_bg

    def __del__(self):

        self.cam.stop()
