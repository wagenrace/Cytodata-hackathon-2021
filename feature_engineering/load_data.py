import pandas as pd
from add_circularity import add_circularity


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
        ]
    )

    return total_biobit


def load_enriched_data(
    loc_good_biobit: str = r"D:\CytoData2021\training_Good.csv",
    loc_bad_biobit: str = r"D:\CytoData2021\training_bad.csv",
):
    total_biobit = load_biobit_features(loc_good_biobit, loc_bad_biobit)
    add_circularity(total_biobit)

    return total_biobit
