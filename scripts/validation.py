from scripts.logger import logger


def validate_dataframe(df):
    """
    Validate the cleaned flight DataFrame.
    Raises ValueError if validation fails.
    """

    if df.empty:
        logger.error("DataFrame is empty.")
        raise ValueError("DataFrame is empty.")

    required_columns = [
        "icao24",
        "callsign",
        "origin_country",
        "longitude",
        "latitude",
        "velocity",
        "last_contact",
    ]

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        logger.error(f"Missing columns: {missing}")
        raise ValueError(f"Missing columns: {missing}")

    logger.info("Data validation passed.")