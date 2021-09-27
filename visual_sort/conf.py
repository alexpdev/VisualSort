# Settings Configuration
TITLE = "Graphical Sorting Demonstrations"
VERSION = 0.3
LICENSE = "GNU GPLv3"
# Activate Debug Mode
DEBUG = False
# Size of window Generated on your screen
SCREEN_SIZE =  (.993,.93,0,0)
# Background Color for screen, defaults to black but can use (r,g,b) values
BACKGROUND =  "black"
# Number of animation to perform per screen update  Default = 1
TRACER = 0
# The speed of pen drawing the vector animation 0-10. Set to 0 for no animation.
SPEED = 0
# Delay for animation to complete.
DELAY = 0
# The Vertical Distance added to each progressive color block
BLOCK_HEIGHT = 8
# Horizantal distance of color block
BLOCK_WIDTH = 16
GRADIENT = ["#e6f060","#ff3311","#440177"]

if DEBUG:
    TRACER = 3
    DELAY = 0
    SPEED = 0
    BLOCK_HEIGHT = 13
    BLOCK_WIDTH = 22
