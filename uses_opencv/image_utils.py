import cv2


def load_binary_image(filename):

    img = cv2.imread(filename)
    if img is None:
        raise RuntimeError('Failed to open "{}"'.format(filename))

    img = img[:, :, 0]
    img = img // 255

    return img


def save_binary_image(filename, img):

    img = img * 255
    retval = cv2.imwrite(filename, img)

    if not retval:
        raise RuntimeError('Failed to save to "{}"'.format(filename))
