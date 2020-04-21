# turtleSort Settings Configuration
TITLE = "Turtle Graphics Sorting Demonstrations"
VERSION = 0.2
LISCENSE = "GNU GPLv3"
# Size of window Generated on your screen
SCREEN_SIZE =  (.96,.92,0,0)
# Background Color for screen, defaults to black but can use (r,g,b) values
BACKGROUND =  "black"
# Number of animation to perform per screen update  Default = 1
TRACER =  10
# The Vertical Distance added to each progressive color block
INCREMENT =  4
# Horizantal distance if color block
WIDTH =  8
"""                         *
                    *       *
            *       *       *
Example: [ ___ ],[ ___ ],[ ___ ]
GAP = 5 WIDTH = 3  INCREMENT = 1
"""



OPTIONS = {
    "size":SCREEN_SIZE,
    "bgcolor":BACKGROUND,
    "tracer":TRACER,
    "dist":WIDTH,
    "inc":INCREMENT,
    }
