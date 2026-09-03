import pandas as pd
import psycopg2

from scripts.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

from scripts.logger import logger


def load_flight_data():

    df = pd.read_csv(
        "/opt/airflow/data/processed/flights_clean.csv"
    )

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

    cursor = conn.cursor()

    inserted = 0

    for _, row in df.iterrows():

        # Convert pandas NaN / NaT to PostgreSQL NULL
        velocity = (
            None
            if pd.isna(row["velocity"])
            else float(row["velocity"])
        )

        baro_altitude = (
            None
            if pd.isna(row["baro_altitude"])
            else float(row["baro_altitude"])
        )

        longitude = (
            None
            if pd.isna(row["longitude"])
            else float(row["longitude"])
        )

        latitude = (
            None
            if pd.isna(row["latitude"])
            else float(row["latitude"])
        )

        last_contact = (
            None
            if pd.isna(row["last_contact"])
            else row["last_contact"]
        )

        time_position = (
            None
            if pd.isna(row["time_position"])
            else row["time_position"]
        )

        flight_date = (
            None
            if pd.isna(row["flight_date"])
            else row["flight_date"]
        )

        cursor.execute(
            """
            INSERT INTO flight_ops.fact_flights
            (
                icao24,
                callsign,
                origin_country,
                longitude,
                latitude,
                baro_altitude,
                velocity,
                on_ground,
                last_contact,
                time_position,
                flight_date
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )
            ON CONFLICT (icao24,last_contact)
            DO NOTHING
            """,
            (
                row["icao24"],
                row["callsign"],
                row["origin_country"],
                longitude,
                latitude,
                baro_altitude,
                velocity,
                row["on_ground"],
                last_contact,
                time_position,
                flight_date,
            ),
        )

        if cursor.rowcount == 1:
            inserted += 1

    conn.commit()

    cursor.close()
    conn.close()

    logger.info(
        f"Inserted {inserted} new records."
    )


if __name__ == "__main__":
    load_flight_data()