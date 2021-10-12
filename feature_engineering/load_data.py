import pandas as pd
from .add_circularity import add_circularity


def load_biobit_features(
    loc_good_biobit: str = r"D:\CytoData2021\training_Good.csv",
    loc_bad_biobit: str = r"D:\CytoData2021\training_bad.csv",
) -> pd.DataFrame:
    # Loading the data and give the column 'is_good' to train on later
    good_biobit = pd.read_csv(loc_good_biobit, index_col="Good_Index")
    good_biobit["is_good"] = True

    bad_biobit = pd.read_csv(loc_bad_biobit, index_col="Bad_Index")
    bad_biobit["is_good"] = False

    total_biobit = pd.concat([good_biobit, bad_biobit])

    # Removing useless columns
    total_biobit = total_biobit.drop(
        columns=[
            "Metadata_TimePoint.1",  # duplicate
            "Metadata_Well.1",  # duplicate
            "Metadata_Series",  # always 1
            "Metadata_Site",  # always 0
            "Metadata_Site.1",  # always 0 and duplicate
            "Metadata_FileLocation",  # always blank
            "Metadata_prefix",  # always blank
            "Location_MaxIntensity_Z_Phase",  # always 0
            "Metadata_Frame",  # always 0
            "Location_CenterMassIntensity_Z_Phase",  # always 0
            "Location_Center_Z",  # always 0
            "Number_Object_Number",  # duplicate
        ]
    )
    # Sample Name
    total_biobit["SampleName"] = total_biobit.index.str.split("_").str[:2].str.join("_")
    total_biobit["ColonyName"] = (
        total_biobit["SampleName"] + "_" + total_biobit["ObjectNumber"].astype(str)
    )

    return total_biobit


def remove_all_location_info(bitbio_data: pd.DataFrame):
    """
    Remove all the location columns make that your model does not train on it.
    If it does it can learn that bad colonies are in the left top or something.
    """
    bitbio_data = bitbio_data.drop(
        columns=[
            "AreaShape_BoundingBoxMaximum_X",
            "AreaShape_BoundingBoxMaximum_Y",
            "AreaShape_BoundingBoxMinimum_X",
            "AreaShape_BoundingBoxMinimum_Y",
            "AreaShape_Center_X",
            "AreaShape_Center_Y",
            "Location_CenterMassIntensity_X_Phase",
            "Location_CenterMassIntensity_Y_Phase",
            "Location_Center_X",
            "Location_Center_Y",
            "Location_MaxIntensity_X_Phase",
            "Location_MaxIntensity_Y_Phase",
        ]
    )
    return bitbio_data


def load_enriched_data(
    loc_good_biobit: str = r"D:\CytoData2021\training_Good.csv",
    loc_bad_biobit: str = r"D:\CytoData2021\training_bad.csv",
):
    total_biobit = load_biobit_features(loc_good_biobit, loc_bad_biobit)
    add_circularity(total_biobit)
    total_biobit["AreaShape_BoundingBoxMaximum_Width"] = total_biobit["AreaShape_BoundingBoxMaximum_X"] - total_biobit["AreaShape_BoundingBoxMinimum_X"]
    total_biobit["AreaShape_BoundingBoxMaximum_Height"] = total_biobit["AreaShape_BoundingBoxMaximum_Y"] - total_biobit["AreaShape_BoundingBoxMinimum_Y"]

    return total_biobit
