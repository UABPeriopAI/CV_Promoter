# config.py
from pathlib import Path

# Development Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
LOGS_DIR = Path(BASE_DIR, "logs")

# Assets
ASSETS_DIR = Path(BASE_DIR, "assets")
TEMPLATE = Path(ASSETS_DIR, "custom-reference.docx")

# Data Directories
DATA_DIR = Path("/data/DATASCI")
RAW_DATA = Path(DATA_DIR, "raw")
INTERMEDIATE_DIR = Path(DATA_DIR, "intermediate")
RESULTS_DIR = Path(DATA_DIR, "results")

NIH_FUNDING_WINDOW = 11

