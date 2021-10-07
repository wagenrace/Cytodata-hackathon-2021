from math import pi


def add_circularity(biobit_df):
    biobit_df["Circularity"] = (4 * pi * biobit_df["AreaShape_Area"]) / (biobit_df["AreaShape_Perimeter"] ** 2)