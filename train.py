#!/usr/bin/env python3

import os
import pathlib

import numpy as np
import tensorflow as tf

from cnn import cnn_model_fn
from local_settings import MODEL_DIR, TRAINING_DATA_DIR


def main(unused_argv):

    training_data_dir = pathlib.Path(TRAINING_DATA_DIR)
    npy_data_dir = training_data_dir / 'npy'
    cwd_old = os.getcwd()
    os.chdir(npy_data_dir)
    train_data = np.load('train_x.npy').astype(np.float32)
    train_labels = np.load('train_y.npy')
    eval_data = np.load('test_x.npy').astype(np.float32)
    eval_labels = np.load('test_y.npy')
    os.chdir(cwd_old)

    run_config = tf.estimator.RunConfig(
        model_dir=MODEL_DIR,
        save_summary_steps=1,
        keep_checkpoint_max=15,
        log_step_count_steps=1,
        train_distribute=None)

    classifier = tf.estimator.Estimator(
        model_fn=cnn_model_fn,
        config=run_config)

    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={'input': train_data},
        y=train_labels,
        batch_size=54,
        num_epochs=None,
        shuffle=True)

    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={'input': eval_data},
        y=eval_labels,
        num_epochs=1,
        batch_size=54,
        shuffle=False)

    tf.logging.set_verbosity(tf.logging.INFO)

    steps = 5
    while(True):
        classifier.train(input_fn=train_input_fn, steps=steps)
        classifier.evaluate(input_fn=eval_input_fn)
        steps = input('\nHow many more steps? ')
        if not steps:
            steps = 5
        else:
            steps = int(steps)
            if steps <= 0:
                break
        print()


if __name__ == '__main__':

    tf.app.run()
