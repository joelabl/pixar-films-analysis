"""This module contains utility functions for the pixarfilms package."""

from pathlib import Path
import os
import requests


def download_pixar_datasets() -> None:
    """Download Pixar datasets from a GitHub repository."""
    target_url = "https://raw.githubusercontent.com/erictleung/pixarfilms/refs/heads/main/data-raw/"

    csv_files = [
        "academy",
        "box_office",
        "genres",
        "pixar_films",
        "pixar_people",
        "public_response",
    ]

    download_dir = Path(__file__).resolve().parent.parent.parent / "data"
    os.makedirs(download_dir, exist_ok=True)

    for file_name in csv_files:
        file_url = f"{target_url}{file_name}.csv"
        try:
            response = requests.get(file_url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as err:
            print(f"Error downloading {file_name}.csv from {file_url}: {err}")
        else:
            file_path = os.path.join(download_dir, f"{file_name}.csv")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Successfully downloaded {file_name}.csv")
