from enum import Enum

COLOR_PALETTE_DARK_PURPLE = ["#000000", "#150050", "#3F0071", "#610094"]
COLOR_PALETTE_DARK_BLUE = ["#26282B", "#353941", "#00A9CB", "#90B8F8"]

COLOR_DARKEST = "#252525"
COLOR_LESS_DARK = "#323232"
GREEN = "#bde9ba"


class ColorsRGB(str, Enum):
    RED = "rgb(245, 124, 103)"
    GREEN = "rgb(189, 233, 186)"
    BLACK = "rgb(50, 56, 62)"


class ColorsHEX(str, Enum):
    RED = "#f57c67"
    GREEN = "#bde9ba"
    BLACK = "#32383e"
