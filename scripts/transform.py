import pandas as pd
import os

from scripts.logger import logger
from scripts.validation import validate_dataframe


def transform_flight_data():

    RAW_FOLDER = "/opt/airflow/data/raw"
    PROCESSED_FOLDER = "/opt/airflow/data/processed"

    os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    # Find raw CSV files
    files = sorted(
        [f for f in os.listdir(RAW_FOLDER) if f.endswith(".csv")]
    )

    if not files:
        raise FileNotFoundError(
            f"No CSV files found in {RAW_FOLDER}"
        )

    latest_file = os.path.join(RAW_FOLDER, files[-1])

    logger.info(f"Reading raw file: {latest_file}")

    # Read raw data
    df = pd.read_csv(latest_file)

    logger.info(f"Raw rows: {len(df)}")

    # --------------------------------------------------
    # Remove duplicate rows
    # --------------------------------------------------
    df.drop_duplicates(inplace=True)

    # --------------------------------------------------
    # Remove rows without coordinates
    # --------------------------------------------------
    df.dropna(
        subset=["latitude", "longitude"],
        inplace=True
    )

    # --------------------------------------------------
    # Clean callsign
    # --------------------------------------------------
    df["callsign"] = (
        df["callsign"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # --------------------------------------------------
    # Convert timestamps
    # --------------------------------------------------
    df["last_contact"] = pd.to_datetime(
        df["last_contact"],
        unit="s",
        errors="coerce"
    )

    df["time_position"] = pd.to_datetime(
        df["time_position"],
        unit="s",
        errors="coerce"
    )

    # --------------------------------------------------
    # Create flight date
    # --------------------------------------------------
    df["flight_date"] = df["last_contact"].dt.date

    # --------------------------------------------------
    # Clean velocity
    # --------------------------------------------------

    df["velocity"] = pd.to_numeric(
    df["velocity"],
    errors="coerce"
    )

    df["velocity"] = df["velocity"].replace(
    [float("inf"), float("-inf")],
    pd.NA
    )


    # --------------------------------------------------
    # Clean altitude
    # --------------------------------------------------

    df["baro_altitude"] = pd.to_numeric(
    df["baro_altitude"],
    errors="coerce"
    )

    df["baro_altitude"] = df["baro_altitude"].replace(
    [float("inf"), float("-inf")],
    pd.NA
    )

    # --------------------------------------------------
    # Explicitly convert NaN to None-compatible values
    # --------------------------------------------------
    df["velocity"] = df["velocity"].replace(
    [float("inf"), float("-inf")],
    pd.NA
    )

    df["baro_altitude"] = df["baro_altitude"].replace(
    [float("inf"), float("-inf")],
    pd.NA
    )

    # --------------------------------------------------
    # Validate dataframe
    # --------------------------------------------------
    validate_dataframe(df)

    # --------------------------------------------------
    # Save processed file
    # --------------------------------------------------
    output_file = os.path.join(
        PROCESSED_FOLDER,
        "flights_clean.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    logger.info(f"Rows after cleaning: {len(df)}")
    logger.info(f"Processed file saved: {output_file}")


if __name__ == "__main__":
    transform_flight_data()