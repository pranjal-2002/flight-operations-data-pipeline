import requests
import pandas as pd
import os
from datetime import datetime
from scripts.logger import logger

# OpenSky API URL
URL = "https://opensky-network.org/api/states/all"


def extract_flight_data():
    logger.info("Fetching live flight data...")

    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    states = data.get("states", [])

    columns = [
        "icao24",
        "callsign",
        "origin_country",
        "time_position",
        "last_contact",
        "longitude",
        "latitude",
        "baro_altitude",
        "on_ground",
        "velocity",
        "true_track",
        "vertical_rate",
        "sensors",
        "geo_altitude",
        "squawk",
        "spi",
        "position_source"
    ]

    df = pd.DataFrame(states, columns=columns)

    os.makedirs("/opt/airflow/data/raw", exist_ok=True)

    filename = f"/opt/airflow/data/raw/flights_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    df.to_csv(filename, index=False)

    logger.info(f"Saved {len(df)} records")
    logger.info(f"Raw file saved: {filename}")


if __name__ == "__main__":
    extract_flight_data()