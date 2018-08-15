import numpy as np
import cv2

from config import (
    CNN_INPUT_IMG_WIDTH, CNN_INPUT_IMG_HEIGHT,
    CAM_RAW_FRAME_WIDTH, CAM_RAW_FRAME_HEIGHT,
)


class CamVision:

    def __init__(self, cam_device_num):

        self.device_num = cam_device_num
        self.cap = cv2.VideoCapture(self.device_num)
        if not self.cap.isOpened():
            raise RuntimeError(
                'Unable to open camera device {}'.format(self.device_num))

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_RAW_FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_RAW_FRAME_HEIGHT)
        if (
            self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) != CAM_RAW_FRAME_WIDTH
            or self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) != CAM_RAW_FRAME_HEIGHT
        ):
            raise RuntimeError(
                'Unable to set camera frame dimensions {}x{} on device {}'
                .format(
                    CAM_RAW_FRAME_WIDTH,
                    CAM_RAW_FRAME_HEIGHT,
                    self.device_num))

        self.learned_bg = None
        self.latest_frame = None
        self.latest_fg_mask = None

    def capture_now(self):

        ret, img = self.cap.read()
        if not ret:
            raise RuntimeError(
                'Failed to read frame from camera device', self.device_num)
        img = cv2.resize(img, (CNN_INPUT_IMG_WIDTH, CNN_INPUT_IMG_HEIGHT))
        self.latest_frame = img.astype(np.uint8)

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

        self.cap.release()
