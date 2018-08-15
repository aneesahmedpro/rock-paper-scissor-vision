#!/usr/bin/env python3

import tensorflow as tf

from local_settings import MODEL_DIR
import config
from config import CNN_INPUT_IMG_WIDTH, CNN_INPUT_IMG_HEIGHT
from cnn import cnn_model_fn
from camvision import CamVision
from gamedisplay import GameDisplay


CAM_DEVICE_NUM = 0
BG_SAMPLES_COUNT = 30


def main():

    # Init camera
    camvision = CamVision(CAM_DEVICE_NUM)

    # Learn the background now so that it can be subtracted from an image
    # later to get the corresponding foreground
    camvision.learn_bg_now(BG_SAMPLES_COUNT)

    # Load the trained Convolutional Neural Network,
    # then bind it to the camera so that it recognises hand postures
    classifier = tf.estimator.Estimator(
        model_fn=cnn_model_fn,
        model_dir=MODEL_DIR)

    def input_generator():
        while True:
            camvision.capture_now()
            camvision.extract_fg()
            cnn_input = camvision.get_latest_fg_mask()
            yield cnn_input

    def input_fn():
        ds = tf.data.Dataset.from_generator(
            input_generator,
            tf.float32,
            tf.TensorShape([CNN_INPUT_IMG_HEIGHT, CNN_INPUT_IMG_WIDTH]))
        feature = ds.make_one_shot_iterator().get_next()
        return {'input': feature}

    output_generator = classifier.predict(input_fn)

    def posture_from_output(output):
        class_id = output['classes']
        class_label = config.CLASS_ID_TO_LABEL[class_id]
        return class_label

    def which_posture_beats_this_posture(posture):
        return config.WHAT_BEATS_WHAT[posture]

    # Determine whether to compete with or follow the user
    competing = not config.COPY_USER_HAND

    # Init game GUI
    game_display = GameDisplay()

    # Capture image, then extract foreground (hand), then display response
    while not game_display.check_quit_key_pressed():
        output = next(output_generator)

        posture = posture_from_output(output)
        if competing:
            game_display.show_repsonse_image(
                which_posture_beats_this_posture(posture))
        else:
            game_display.show_repsonse_image(posture)

        fg_mask_img = camvision.get_latest_fg_mask() * 255
        game_display.show_camvision_image(fg_mask_img)


if __name__ == '__main__':

    main()
