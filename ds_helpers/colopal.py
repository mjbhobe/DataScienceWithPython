"""colopal.py: colors & palettes"""
import re
from typing import Tuple, Union
from pprint import pprint

ColorTupleType = Tuple[int, int, int]

# favourite color palette
FAV_COLORS = [
    "#64E6FF",
    "#007DC5",
    "#4D2F9E",
    "#BE0046",
    "#EB5000",
    "#FFE600",
    "#02D46A",
]


def hex2rgb(color: str) -> str:
    # hex_color is like '#aabbcc' returns -> "rgb(r,g,b)""
    hexpat = r"#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})"
    match = re.match(hexpat, color)
    if match:
        return f"rgb({int(match.group(1),16)},{int(match.group(2),16)},{int(match.group(3),16)})"
    raise TypeError(f"{color} does not match hex color pattern '#rrggbb'")


def rgb2hex(color: Union[ColorTupleType, str]):
    # rgb_color is like (r,g,b) [tuple of ints] or "rgb(r,g,b)", returns "#rrggbb"
    if isinstance(color, tuple):
        r, g, b = color
        # return f"#{str(hex(r))[2:]}{str(hex(g))[2:]}{str(hex(b))[2:]}"
        return f"#{r:02x}{g:02x}{b:02x}"
    else:
        pattern = re.compile(r"rgb\((?:(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*)\)")
        match = re.match(pattern, color)
        if match:
            r, g, b = match.group(1), match.group(2), match.group(3)
            return (
                # f"#{str(hex(int(r)))[2:]}{str(hex(int(g)))[2:]}{str(hex(int(b)))[2:]}"
                f"#{int(r):02x}{int(g):02x}{int(b):02x}"
            )
        raise TypeError(f"{color} does not confirm to rgb(...) color format!")


def convert_string_color_to_hex(color):
    match = re.match(r"#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})", color)
    if match:
        return match.group(1) + match.group(2) + match.group(3)
    else:
        return None


def __get_rgb_from_color(color):
    """get individual colors from color pattern
    @params:
        color - the color to parse
            can be in hex ("#rrggbb") or rgb ("rgb(rr,gg,bb)") format only
    """
    hex_pat = re.compile(r"#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})")
    rgb_pat = re.compile(r"rgb\((?:(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*)\)")

    hex_match = re.match(hex_pat, color)
    rgb_match = re.match(rgb_pat, color)

    if hex_match:
        r, g, b = (
            int(hex_match.group(1), 16),
            int(hex_match.group(2), 16),
            int(hex_match.group(3), 16),
        )
    elif rgb_match:
        r, g, b = (
            int(rgb_match.group(1)),
            int(rgb_match.group(2)),
            int(rgb_match.group(3)),
        )
    else:
        raise TypeError(
            f"{color} does not confirm to RGB (rgb(r,g,b)) or hex (#rrggbb) format!"
        )

    return (r, g, b)


def lighten_color(color, factor, return_as_hex=True):
    """Lightens the given color by the specified amount.

    Args:
        color (str): The color to lighten.
            can be in hex ("#rrggbb") or rgb ("rgb(rr,gg,bb)" format)
        amount (float): The amount to lighten the color by.
            if amount = 0.75, color is lightened by 75%

    Returns:
        str: The lightened color.
    """

    r, g, b = __get_rgb_from_color(color)
    r = int(255 - (255 - r) * (1 - factor))
    g = int(255 - (255 - g) * (1 - factor))
    b = int(255 - (255 - b) * (1 - factor))

    if return_as_hex:
        ret = rgb2hex((r, g, b))
    else:
        ret = f"rgb({r},{g},{b})"
    return ret


def darken_color(color, factor, return_as_hex=True):
    """darkens the given color by the specified amount.

    Args:
        color (str): The color to lighten.
            can be in hex ("#rrggbb") or rgb ("rgb(rr,gg,bb)" format)
        amount (float): The amount to lighten the color by.
            if amount = 0.75, color is lightened by 75%

    Returns:
        str: The lightened color.
    """

    r, g, b = __get_rgb_from_color(color)
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)

    if return_as_hex:
        ret = rgb2hex((r, g, b))
    else:
        ret = f"rgb({r},{g},{b})"
    return ret


def palettes_from_colors(colors: list):
    """
    create a palette of colors like in Microsoft office, where we
    have the color & 5 accents of each color
        - 80% lighter, 60% lighter, 40% lighter, 25% darker and 50% darker

    palatte if created like this:
    color_palette {
        "original" : [the list of colors you pass in]
        "lighter_80p" : [each color from above list lightened by 80%]
        "lighter_60p" : [each color from above list lightened by 80%]
        "lighter_40p" : [each color from above list lightened by 80%]
        "darker_25p" : [each color from above list darkened by 25%]
        "darker_50p" : [each color from above list darkened by 50%]
    }
    """
    color_palette = {
        "original": colors,
        "lighter_80p": [],
        "lighter_60p": [],
        "lighter_40p": [],
        "darker_25p": [],
        "darker_50p": [],
    }
    for color in colors:
        lighter_80p = lighten_color(color, 0.80)
        lighter_60p = lighten_color(color, 0.60)
        lighter_40p = lighten_color(color, 0.40)
        darker_25p = darken_color(color, 0.25)
        darker_50p = darken_color(color, 0.50)
        color_palette["lighter_80p"].append(lighter_80p)
        color_palette["lighter_60p"].append(lighter_60p)
        color_palette["lighter_40p"].append(lighter_40p)
        color_palette["darker_25p"].append(darker_25p)
        color_palette["darker_50p"].append(darker_50p)
    return color_palette


if __name__ == "__main__":
    assert rgb2hex((245, 67, 155)) == "#f5439b"
    assert rgb2hex("rgb(245, 67, 155)") == "#f5439b"
    assert hex2rgb("#f5439b") == "rgb(245,67,155)"
    color = "rgb(71,163,255)"
    lightened_80p = lighten_color(color, 0.8, False)
    lightened_60p = lighten_color(color, 0.6, False)
    lightened_40p = lighten_color(color, 0.4, False)
    darker_25p = darken_color(color, 0.25, False)
    darker_50p = darken_color(color, 0.50, False)
    print(
        f"{color} lightened: by 80%: {lightened_80p} - by 60%: {lightened_60p} - by 40%: {lightened_40p}"
    )
    print(f"{color} darkened: by 25%: {darker_25p} - by 50%: {darker_50p}")

    color_palette = palettes_from_colors(
        ["#64E6FF", "#007DC5", "#4D2F9E", "#BE0046", "#EB5000", "#FFE600"]
    )
    pprint(color_palette)
