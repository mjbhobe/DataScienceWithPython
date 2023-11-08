version_info = (1, 0, 0, "dev0")

__version__ = ".".join(map(str, version_info))
__installer_version__ = __version__
__title__ = "Data Science Helpers"
__author__ = "Manish Bhobé"
# Nämostuté -> means "May our Minds Meet"
__organization__ = "Nämostuté Ltd."
__org_domain__ = "namostute.pytorch.in"
__license__ = __doc__
__project_url__ = "https://github.com/mjbhobe/DataScienceWithPython"

__FAV_SEED = 41


def about():
    about_info = (
        f"{__title__} by {__author__}. Released by {__organization__} with MIT Licence.\n"
        f"Use at your own risk. {__author__} (or {__organization__}) are not liable for any damages from use of this software!"
    )
    return about_info


from .colopal import (
    FAV_COLORS,
    hex2rgb,
    rgb2hex,
    lighten_color,
    darken_color,
    palettes_from_colors,
)
