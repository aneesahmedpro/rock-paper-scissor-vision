## How to Install

1.  Make sure the camera works by using any camera application and capturing
    some test photos and videos.

1.  Install Python on your system and make sure it is working. Test it by
    launching the interpreter:

    +   On Linux: \
        `python3`

    +   On Windows: \
        `py -3`

1.  Read the section "PyGame vs OpenCV" in [`README.md`](./README.md) and
    decide whether you want to integrate this project with PyGame library or
    OpenCV library.

    Subsequent steps depend on the choice you make now.

1.  Download the project source code to any directory on your system. Assume
    that the directory is `/whatever/the/path`.

1.  Change the working directory to the project root directory: \
    `cd /whatever/the/path/rock-paper-scissor-vision`

    All the subsequent instructions are assuming you are in the project root
    directory.

1.  Now to install the required packages, there are many ways to do it. The
    best method is to use [virtual environments][python-tutorial-venv], as
    it keeps the project environment and system-wide environment isolated from
    each- other. Read up on them and go through some tutorials if you don't
    know how to use them.

    1.  Create a fresh virtual environment with name `virtenv`:

        +   On Linux: \
        `python3 -m venv virtenv`

        +   On Windows: \
        `py -3 -m venv virtenv`

        **NOTE** \
        This isolation between system-wide environment and project environment
        can cause problems in some specific cases. For example, if you are on
        Ubuntu and you chose OpenCV, you would install it via APT: \
        `sudo apt install python3-opencv` \
        But APT installs it into the system-wide environment, and hence the
        virtual environment cannot access it. To work around this, you must
        create the kind of virtual environment which can access the libraries
        installed in the system-wide environment: \
        `python3 -m venv --system-site-packages virtenv`

    1.  Activate the virtual environment:

        +   On Linux (for Bash shell only): \
        `source virtenv/bin/activate`

        +   On Windows: \
        `virtenv\Scripts\activate.bat`

1.  Install TensorFlow: \
    `pip install tensorflow`

1.  Install NumPy: \
    `pip install numpy`

1.  Now you have to install either OpenCV or PyGame:

    +   If you decided to use PyGame:

        Simply install it via pip: \
        `pip install pygame`

    +   If you decided to use OpenCV:

        +   On Ubuntu:

            Install via APT: \
            `sudo apt install python3-opencv`

            **WARNING** \
            APT installs the libraries to the system-wide environment. \
            See the **NOTE** in the step above where the instructions for
            creating a virtual environment were given. \
            If you missed the NOTE and created the virtual environment without
            the `--system-site-packages` option, you've messed up. Destroy the
            virtual environment by deleting the `virtenv` directory. Now do the
            step of creating the virtual environment correctly this time by
            following the NOTE and then repeat all the steps after it.

        +   On Windows:

            For easy installation, you should use the (unofficial) wheel of
            OpenCV library built by Christoph Gohlke. Click
            [here][gohlke-opencv] to go to the download page.

            Download the version that matches your Python setup.
            e.g. Filename `opencv_python-3.4.1-cp36-cp36m-win_amd64.whl` means:

            +   OpenCV library version is 3.4.1
            +   Python software version must be 3.6
            +   `win_amd64` means 64-bit, `win32` means 32-bit.

            After downloading, install it: \
            `pip install /path/to/opencv_python-3.4.1-cp36-cp36m-win_amd64.whl`

        +   On Others:

            Search online for instructions on how to install OpenCV on your
            platform and make it accessible to Python. You might have to
            compile OpenCV from sources yourself.

1.  Now you have to copy some files into the root project directory:

    +   If you decided to use PyGame:

        Copy all the files from the `uses_pygame` directory:

        +   On Linux: \
            `cp uses_pygame/* ./`

        +   On Windows: \
            `xcopy uses_pygame\* .`

    +   If you decided to use OpenCV:

        Copy all the files from the `uses_opencv` directory:

        +   On Linux: \
            `cp uses_opencv/* ./`

        +   On Windows: \
            `xcopy uses_opencv\* .`

1.  Make sure the GUI components work by executing `test_gamedisplay`.py:

    +   On Linux: \
        `./test_gamedisplay.py`

    +   On Windows: \
        `py -3 test_gamedisplay.py`

1.  Make sure the camera integration works by executing `test_camvision`.py:

    +   On Linux: \
        `./test_camvision.py`

    +   On Windows: \
        `py -3 test_camvision.py`


## How to Play

1.  Make sure the room is well-lit, and not very dark.

1.  Find a good background. A good background...

    +   is mostly the same colour everywhere, e.g. a uniformly painted wall.
    +   is fully static/frozen. Nothing should be moving in the frame.
    +   is different shade of colour than your skin.

1.  Point the camera at the static background. If it's the laptop webcam,
    adjust your laptop such that webcam points at the static background.

1.  Make sure you yourself (or any body part, or some other object) are not
    in front of the camera.

1.  Launch the application by executing `play.py`:

    +   On Linux: \
        `./play.py`

    +   On Windows: \
        `py -3 play.py`

1.  Wait for a couple of seconds. The machine is observing the background so
    that later it can tell if your hand is in front of the background.

1.  A window will popup. On the left will be what the machine is looking at,
    and on the right, what is its response.

    It should be a static black image on the left. \
    If there are a lot of speckles all over the image, or some white shapes,
    or some other kind of noises, then the machine has failed to properly
    observe and judge the background.

    Things you can try to fix it:

    +   Restart the program. (Sometimes the camera changes its exposure at
        startup to adjust to the lighting and hence the machine gets
        confused.)

    +   Increase the lighting/brightness of the room. Then restart.

    +   Remove from in front the camera anything that might be slightly
        moving, oscillating, etc. Then restart.

1.  Now put your hand in front of the camera. It should show up as white.

    Make sure your hand is upright. See the training images in the directory
    `training_data` to get an idea of what the machine is trained for.

    If the white shape of the hand is not showing up as very sharp and clear,
    the mahcine will fail to recognise it.

    Things you can try to fix it:

    +   Move your hand away from the background. If you are too near the
        background, the shadow cast by your hand onto the background will
        confuse the foreground-background separation algorithm.

    +   Make sure there aren't any strong edges formed at the boundaries of
        two objects with different colours, in the viewport of the camera.
        Try a very plain uniformly coloured wall in an uniformly lit room.

    +   Make sure the colour of background is not too similar to the colour
        of your skin.

1.  Make any posture (rock, paper or scissor) with your hand and the machine
    will respond by showing you an image of hand in that posture that beats
    your posture.

    You can play as long as you want. Just change the posture and the machine
    will respond in real-time.

1.  When you want to quit the program, press the `ESC` button.


[python-tutorial-venv]: https://docs.python.org/3/tutorial/venv.html
[gohlke-opencv]: https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv


## **Bonus**: How to Train the Model yourself

Playing is fun. But if you want, you can train the model yourself from scratch!
The training data is already present in the directory `training_data`.

But you must have some experience in machine learning, otherwise you will have
no idea what is going on.

The taining data is in the form of [PNG][png] images. You can look at them if
you want. This is the directory tree structure of `training_data`:

    training_data
    ├── npy
    └── raw
        ├── test
        │   ├── paper
        │   ├── rock
        │   └── scissor
        └── train
            ├── paper
            ├── rock
            └── scissor

The images are being called raw data here because we will be converting them in
another format later which is more suitable for fast loading and training.

So in the `raw` directory the data is divided as "for training" and "for
testing/validation/evaluation" as usual. The directories are named `train` and
`test`, and inside of each of them are three directories `rock`, `paper` and
`scissor`. Each of those contain 90 PNG images.

1.  Change the working directory to the project root directory: \
    `cd /whatever/the/path/rock-paper-scissor-vision`

    All the subsequent instructions are assuming you are in the project root
    directory.

1.  The `npy` directory might be missing on your disk. Especially if you have
    freshly cloned the repository.

    Create it if it indeed is missing:

    +   On Linux: \
        `mkdir training_data/npy`

    +   On Windows: \
        `mkdir training_data\npy`


1.  Compile the data into [NPY][npy] container files by executing `compile.py`:

    +   On Linux: \
        `./compile.py`

    +   On Windows: \
        `py -3 compile.py`

    If successful, the command will create these data files in the
    `training_data/npy` directory:

    +   `train_x.npy`
    +   `train_y.npy`
    +   `test_x.npy`
    +   `test_y.npy`

    The filenames are pretty self-explanatory.

1.  Delete the directory `cnn_tf_model` so that we can start training from
    scratch.

1.  Begin the training by executing `train.py`:

    +   On Linux: \
        `./train.py`

    +   On Windows: \
        `py -3 train.py`

1.  In the given default training data, each class has 90 images, hence a total
    of 270 images. I have set the batch size to be 54 images in `train.py`. So,
    each epoch is 5 steps.

    After initial loading, `train.py` will run 5 steps (= 1 epoch), then
    evaluate the model and print some accuracy statistics.

    It will then prompt, asking how many more steps should it perform. You can
    enter whatever you want. It will again train for those many steps, evaluate
    the model and print some accuracy statistics.

    When you want to quit, just enter 0 (zero) in the prompt.

    However, quiting doesn't mean you will have to start-over from scratch the
    next time. If you execute `train.py` again, it will just resume the
    training from where it left off. You can see the model checkpoints being
    saved in the console log output.

    Train the model enough so that it has very good accuracy. It took me
    a total of 19 steps to achieve accuracy of 100% on the test dataset.
    However be careful not to over-train the model. Once in the 98%-100%
    accurace range, it is very easy to accidently go into the over-learning
    phase.

1.  After training has finished, you can run the model by playing, as you did
    in the section "How to Play" above.


[png]: https://en.wikipedia.org/wiki/Portable_Network_Graphics
[npy]: https://docs.scipy.org/doc/numpy/neps/npy-format.html


## **Bonus**: How to Create the Training Data yourself

Instead of using the default training data, you can create your own training
data and train the model on it.

1.  Delete all the images in the directory `training_data`. But be careful not
    delete any directory, as that will alter the directory tree structure.

1.  (Optional) Delete the NPY files in the `training_data/npy` directory.
    Even if you don't, they will be overwritten by `compile.py` anyway.

1.  Capture all the images you want by executing `create.py`:

    +   On Linux: \
        `./create.py`

    +   On Windows: \
        `py -3 create.py`

1.  You will see what you are capturing in the window popup.

1.  When you want to quit, press the `ESC` button.

1.  Look inside the newly created `captures` directory. These are all the
    frames captured.

1.  You have to create a good dataset for training from these images. You are
    on your own for this task.

1.  When done, separate the data into "test" and "train" dataset.

    Then further divide each of those datasets into three classes: "rock",
    "paper" and "scissor".

1.  Now arrange all the images into the `training_data/raw` directory correctly
    similar to how the default training data images were arranged.

    Remember not to disturb the directory tree structure of `training_data`.

1.  Now you can train on it as you did in the section "How to Train the Model
    yourself" above.
