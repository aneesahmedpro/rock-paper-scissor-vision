import tensorflow as tf


def cnn_model_fn(features, labels, mode):

    input_layer = tf.reshape(features['input'], (-1, 120, 160, 1))

    # shape: (?, 120, 160, 1)

    conv1 = tf.layers.conv2d(
        inputs=input_layer,
        filters=64,
        kernel_size=16,
        padding='same',
        activation=tf.nn.relu)

    # shape: (?, 120, 160, 64)

    pool1 = tf.layers.max_pooling2d(
        inputs=conv1,
        pool_size=16,
        strides=16,
        padding='same')

    # shape: (?, 8, 10, 64)

    conv2 = tf.layers.conv2d(
        inputs=pool1,
        filters=64,
        kernel_size=8,
        padding='same',
        activation=tf.nn.relu)

    # shape: (?, 8, 10, 64)

    pool2 = tf.layers.max_pooling2d(
        inputs=conv2,
        pool_size=8,
        strides=8,
        padding='same')

    # shape: (?, 1, 2, 64)

    flat = tf.reshape(pool2, (-1, 1 * 2 * 64))

    # shape: (?, 1*2*64)

    dense = tf.layers.dense(inputs=flat, units=1024, activation=tf.nn.relu)

    # shape: (?, 1024)

    dropout = tf.layers.dropout(
        inputs=dense,
        rate=0.4,
        training=(mode == tf.estimator.ModeKeys.TRAIN))

    # shape: (?, 1024)

    logits = tf.layers.dense(inputs=dropout, units=3)

    # shape: (?, 3)

    predicted_classes = tf.argmax(input=logits, axis=1)
    predicted_probabilities = tf.nn.softmax(logits)

    prediction_data = {
        'classes': predicted_classes,
        'probabilities': predicted_probabilities,
    }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode, prediction_data)

    loss_op = tf.losses.sparse_softmax_cross_entropy(labels, logits)

    accuracy = tf.metrics.accuracy(labels, predicted_classes)
    rms_error = tf.metrics.root_mean_squared_error(labels, predicted_classes)

    eval_metric_ops = {
        'accuracy': accuracy,
        'root_mean_squared_error': rms_error,
    }

    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(
            loss=loss_op,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(
            mode=mode, loss=loss_op, train_op=train_op)

    if mode == tf.estimator.ModeKeys.EVAL:
        return tf.estimator.EstimatorSpec(
            mode=mode, loss=loss_op, eval_metric_ops=eval_metric_ops)
