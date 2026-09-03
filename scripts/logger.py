import logging
import os

LOG_DIR = "/opt/airflow/logs"

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/flight_pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("flight_pipeline")