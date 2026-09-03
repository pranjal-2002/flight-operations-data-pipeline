CREATE SCHEMA IF NOT EXISTS flight_ops;

CREATE TABLE IF NOT EXISTS flight_ops.live_flights (
    id SERIAL PRIMARY KEY,
    icao24 VARCHAR(20),
    callsign VARCHAR(20),
    origin_country VARCHAR(100),
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    baro_altitude DOUBLE PRECISION,
    velocity DOUBLE PRECISION,
    on_ground BOOLEAN,
    last_contact TIMESTAMP,
    snapshot_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS flight_ops.airports (
    airport_id SERIAL PRIMARY KEY,
    airport_code VARCHAR(10),
    airport_name VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS flight_ops.airlines (
    airline_id SERIAL PRIMARY KEY,
    airline_code VARCHAR(10),
    airline_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS flight_ops.fact_flights (
    id SERIAL PRIMARY KEY,
    icao24 VARCHAR(20),
    callsign VARCHAR(20),
    origin_country VARCHAR(100),
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    baro_altitude DOUBLE PRECISION,
    velocity DOUBLE PRECISION,
    on_ground BOOLEAN,
    last_contact TIMESTAMP,
    time_position TIMESTAMP,
    flight_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);