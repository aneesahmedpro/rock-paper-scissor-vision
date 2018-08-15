CNN_INPUT_IMG_WIDTH = 160
CNN_INPUT_IMG_HEIGHT = 120

CAM_RAW_FRAME_WIDTH = 320
CAM_RAW_FRAME_HEIGHT = 240

# COPY_USER_HAND is a bool
# True: if user makes rock, computer makes rock
# False: if user makes rock, computer makes paper
COPY_USER_HAND = False

CLASS_ID_TO_LABEL = {
    0: 'rock',
    1: 'paper',
    2: 'scissor',
}

CLASS_LABEL_TO_ID = {v: k for k, v in CLASS_ID_TO_LABEL.items()}

WHAT_BEATS_WHAT = {  # "value" beats "key"
    'rock': 'paper',
    'paper': 'scissor',
    'scissor': 'rock',
}
