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
TRACER = 75
# The speed of pen drawing the vector animation 0-10. Set to 0 for no animation.
SPEED = 0
# Delay for animation to complete.
DELAY = 0
# The Vertical Distance added to each progressive color block
BLOCK_HEIGHT = 5
# Horizantal distance of color block
BLOCK_WIDTH = 10

GRADIENT = ["#ffffff", "#e6f060", "#00ffff", "#ff3311", "#00ff00",
            "#0000ff", "#ffff00", "#ff0000", "#6666f6", "#440177", "#137c63"]

if DEBUG:
    TRACER = 3
    DELAY = 0
    SPEED = 0
    BLOCK_HEIGHT = 13
    BLOCK_WIDTH = 22
