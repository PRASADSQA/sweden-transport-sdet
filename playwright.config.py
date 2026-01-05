import os

BASE_URL = "https://www.sl.se"  # Example: Sweden Public Transport (SL)

def pytest_configure(config):
    config.option.base_url = BASE_URL
