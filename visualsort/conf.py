from copy import deepcopy
import os
import configparser



def configuration():
    parser = configparser.ConfigParser()
    config = None
    for filename in os.listdir(os.getcwd()):
        if os.path.splitext(filename)[-1] == ".ini":
            parser.read_file(open(filename), filename)
            if "VisualSort" in parser:
                config = parser["VisualSort"]
                break
    if not config:
        config = CONFIG
        return config
    for k, v in config.items():
        if k == "gradient":
            value = v.split(",")
        elif k == "screensize":
            value = tuple([float(i.strip()) for i in v.split("\n") if i])
        elif v.isdigit():
            value = int(v)
        else:
            value = v
        try:
            CONFIG[k] = value
        except KeyError:
            pass
    config = deepcopy(CONFIG)
    return config


# Default configuration values
CONFIG = {
    "screensize": (.993,.93,0,0),
    "background": "black",
    "tracer": 3,
    "speed": 0,
    "delay": 0,
    "blockheight": 13,
    "blockwidth": 22,
    "gradient": [
        "#ffffff",
        "#e6f060",
        "#00ffff",
        "#ff3311",
        "#00ff00",
        "#0000ff",
        "#ffff00",
        "#ff0000",
        "#6666f6",
        "#440177",
        "#137c63"
    ]
}
