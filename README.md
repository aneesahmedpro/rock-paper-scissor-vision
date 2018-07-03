# Rock-Paper-Scissor Vision

Make the machine look at the hand of a person using live camera feed and
recognise the postures made by the hand (rock, paper or scissor) in realtime
using a convolutional neural network.

----

## System Requirements

1.  A camera device (e.g. the in-built webcam of laptop)
1.  Python (3.6 or higher)
1.  Numpy (1.13.3 or higher)
1.  TensorFlow (1.8 or higher)
1.  Either one of the following:
    1.  PyGame (1.9.3 or higher)
    1.  OpenCV (3.2.0 or higher)


## PyGame vs OpenCV

To access the camera and to show the GUI windows on screen, a library is
required which is capable of all that. This project currently supports 2
libraries: PyGame and OpenCV. Either one can be used.

To help you choose, here is a comparision:

OpenCV advantages:

+   Works well on a variety of platforms, including Linux and Windows.

OpenCV disadvantages:

+   Being a full-fledged computer vision library, it is too huge and heavy for
    a small task of accessing camera. The wheel is around 40 MB in size.
+   Can be a huge hassle to install and get it working. But for many platforms
    it has been made a lot easier to setup, e.g. on Windows and on Ubuntu.

PyGame advantages:

+   Being a light-weight game development library, the wheel file is small and
    only around 5 MB in size.

PyGame disadvantages:

+   The camera accessing feature is (currently) experimental and maybe be
    removed in the future.
+   The camera accessing feature currently only works on Linux platforms.


## How to Install:

See the section "How to Install" in [`INSTRUCTIONS.md`](./INSTRUCTIONS.md).
