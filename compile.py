#!/usr/bin/env python3

import os
import pathlib

import numpy as np

from config import CLASS_LABEL_TO_ID
from local_settings import TRAINING_DATA_DIR
from image_utils import load_binary_image


CLASS_LABELS = ['rock', 'paper', 'scissor']


def verify_dir(directory):

    if directory.exists():
        if directory.is_dir():
            print('[  OK  ] "{}" is present'.format(str(directory)))
            return True
        else:
            print('[ FAIL ]"{}" is not a directory'.format(str(directory)))
            return False
    else:
        print('[ FAIL ] "{}" is missing'.format(str(directory)))
        return False


def verify_directory_tree(training_data_dir):

    raw_images_dir = training_data_dir / 'raw'
    test_images_dir = raw_images_dir / 'test'
    train_images_dir = raw_images_dir / 'train'
    npy_data_dir = training_data_dir / 'npy'

    results = []

    results.append(verify_dir(training_data_dir))
    results.append(verify_dir(raw_images_dir))
    results.append(verify_dir(test_images_dir))
    results.append(verify_dir(train_images_dir))

    for class_label in CLASS_LABELS:
        results.append(verify_dir(test_images_dir / class_label))

    for class_label in CLASS_LABELS:
        results.append(verify_dir(train_images_dir / class_label))

    results.append(verify_dir(npy_data_dir))

    tree_structure_correct = all(results)

    if tree_structure_correct:
        return test_images_dir, train_images_dir, npy_data_dir
    else:
        return None


def load_training_data(container_dir):

    x, y = [], []
    for class_label in CLASS_LABELS:
        class_images_dir = container_dir / class_label
        for img_file in class_images_dir.iterdir():
            img = load_binary_image(str(img_file))
            class_id = CLASS_LABEL_TO_ID[class_label]
            x.append(img)
            y.append(class_id)
    return x, y


def main():

    training_data_dir = pathlib.Path(TRAINING_DATA_DIR)

    print('Verifying the directory tree structure...\n')
    returned = verify_directory_tree(training_data_dir)
    if returned is None:
        print('\nVerification failed\n')
        return
    else:
        print('\nVerification successful\n')
        test_images_dir, train_images_dir, npy_data_dir = returned

    train_x, train_y = load_training_data(train_images_dir)
    test_x, test_y = load_training_data(test_images_dir)

    os.chdir(npy_data_dir)
    np.save('train_x.npy', train_x, allow_pickle=False)
    np.save('train_y.npy', train_y, allow_pickle=False)
    np.save('test_x.npy', test_x, allow_pickle=False)
    np.save('test_y.npy', test_y, allow_pickle=False)

    print('Data successfully compiled into npy containers.')


if __name__ == '__main__':

    main()
