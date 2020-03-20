import os
import sys
from pathlib import Path

this_file = Path(__file__).resolve()
this_file_dir = this_file.parent
Base = os.path.dirname(this_file_dir)
sys.path.append(Base)

from turtleSort.main import main
from turtleSort.config import OPTIONS
from turtleSort.prep import setup

def start(**kwargs):
    seq,screen = setup(**kwargs)
    main(seq)
    screen.mainloop()

if __name__ == "__main__":
    kwargs = OPTIONS
    kwargs["gradient"] = ((255,12,0),(18,84,255))
    kwargs["size"] = (.9,.9)
    start(**kwargs)

