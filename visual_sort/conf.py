# Settings Configuration
TITLE = "Graphical Sorting Demonstrations"
VERSION = 0.3
LICENSE = "GNU GPLv3"
# Size of window Generated on your screen
SCREEN_SIZE =  (.993,.93,0,0)
# Background Color for screen, defaults to black but can use (r,g,b) values
BACKGROUND =  "black"
# Activate Debug Mode
DEBUG = False
# Number of animation to perform per screen update  Default = 1
TRACER = 9
# The speed of pen drawing the vector animation 0-10. Set to 0 for no animation.
SPEED = 0
# Delay for animation to complete.
DELAY = 0
# The Vertical Distance added to each progressive color block
BLOCK_HEIGHT = 9
# Horizantal distance of color block
BLOCK_WIDTH = 15

if DEBUG:
    TRACER = 3
    DELAY = 0
    SPEED = 0
    BLOCK_HEIGHT = 13
    BLOCK_WIDTH = 22
