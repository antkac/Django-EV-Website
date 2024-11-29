from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def map_tow_hitch(value: str) -> bool:
    return True if value == "Towbar possible" else False


def map_drive_config(value: str) -> str:
    mapping = {
        "Rear Wheel Drive": "RWD",
        "All Wheel Drive": "AWD",
        "Front Wheel Drive": "FWD"
    }
    return mapping.get(value, "Unknown")


def unify_car_value(df: pd.DataFrame) -> pd.DataFrame:
    """ All rows with missing DE pricing have US price present. """
    filter = df["value"] == 0
    df.loc[filter, "value"] = (df.loc[filter, "Estimated_US_Value"] * 0.96).astype(int)
    return df


def save_to_csv(df: pd.DataFrame):
    output_file = DATA_DIR / "processed_cars_data.csv"
    try:
        df.to_csv(output_file, index=False)
        print(f"Processed data saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")


def process_csv(csv_path: str):
    use_cols = ['Brand', 'Model', 'Battery', "km_of_range", '0-100', 'Top_Speed', 'Range', 'Efficiency', 'Fastcharge',
                'Germany_price_before_incentives', 'Netherlands_price_before_incentives', 'Drive_Configuration',
                'Tow_Hitch',
                'Number_of_seats', 'Estimated_US_Value'
                ]
    try:
        raw_df = pd.read_csv(DATA_DIR / csv_path, usecols=use_cols)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    renamed_df = raw_df.rename(columns={
        "Brand": "make",
        "Model": "name",
        "Battery": "battery",
        "Range": "real_range",
        "Efficiency": "efficiency",
        "Fastcharge": "charge_power",
        "Drive_Configuration": "drive",
        "Number_of_seats": "seats",
        "Tow_Hitch": "tow_hitch",
        "Top_Speed": "top_speed",
        "0-100": "acceleration",
        "Germany_price_before_incentives": "value"
    }).assign(
        tow_hitch=lambda df: df["tow_hitch"].map(map_tow_hitch),
        drive=lambda df: df["drive"].map(map_drive_config)
    )

    processed_df = unify_car_value(renamed_df)[["make", "name", "battery", "real_range", "efficiency", "charge_power",
                                                "drive", "seats", "tow_hitch", "top_speed", "acceleration", "value"]]
    save_to_csv(processed_df)


process_csv("raw_cars_data.csv")
