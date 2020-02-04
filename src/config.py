# turtleSort Settings Configuration
TITLE = "Turtle Graphics Sorting Demonstrations"
VERSION = 0.1
LISCENSE = "MIT"
# Size of window Generated on your screen
SCREEN_SIZE =  (.6,.8)
# Location of the window generated on your screen
SCREEN_POSITION = (0,0)
# Background Color for screen, defaults to black but can use (r,g,b) values
BACKGROUND =  "black"
# COLORMODE of the screen options are 0-1 or 0-255
COLORMODE =  255
# Speed of animations
SPEED =  0
# If True then It will generate a random color of each unit instead of gradient
RANDOM_COLOR = False
# Number of animation to perform per screen update  Default = 1
TRACER =  1
# The speed of the animations
DELAY =  0
# Color range for Gradient Color Scheme
GRADIENT =  [(245,10,77),(100,84,90)]
# The Vertical Distance added to each progressive color block
INCREMENT =  7
# Horizontal distance of the individual units in sequence
GAP =  10
# Horizantal distance if color block
WIDTH =  7
"""                         *
                    *       *
            *       *       *
Example: [ ___ ],[ ___ ],[ ___ ]
GAP = 5 WIDTH = 3  INCREMENT = 1
"""



OPTIONS = {"size":SCREEN_SIZE,"random":RANDOM_COLOR,"s_pos":SCREEN_POSITION,"bgcolor":BACKGROUND,"colormode":COLORMODE,"speed":SPEED,"tracer":TRACER,"delay":DELAY,"gradient":GRADIENT,"width":WIDTH,"inc":INCREMENT,"gap":GAP}
