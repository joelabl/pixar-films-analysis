"""Module for loading Pixar films datasets.

This module provides a unified interface to load various Pixar-related CSV datasets.
It supports caching and allows the user to specify a custom data directory.

Example usage:
    from pixarfilms.datasets import load_academy, load_dataset

    # Sklearn-style:
    df_academy = load_academy(as_frame=True)
    df_genres = load_genres()

    # Seaborn-style:
    df_box_office = load_dataset("box_office", cache=True, data_home=None, as_frame=True)
"""

from pathlib import Path
from typing import Optional, Union, Dict

import numpy as np
import pandas as pd

# Global cache for loaded datasets.
_CACHE: Dict[str, pd.DataFrame] = {}

# Mapping of dataset names to their corresponding CSV filenames.
_DATASETS: Dict[str, str] = {
    "academy": "academy.csv",
    "genres": "genres.csv",
    "films": "pixar_films.csv",
    "people": "pixar_people.csv",
    "public_response": "public_response.csv",
    "box_office": "box_office.csv",
}


def _get_default_data_home() -> Path:
    """Determine the default data directory relative to this file.

    Returns:
        Path: The default data directory (assumed to be at the project root under 'data').
    """
    return Path(__file__).resolve().parent.parent.parent / "data"


def load_dataset(
    name: str,
    cache: bool = True,
    data_home: Optional[str] = None,
    as_frame: bool = True,
) -> Union[pd.DataFrame, np.ndarray]:
    """Load a Pixar films dataset by name.

    Args:
        name (str): The name of the dataset to load. Valid options are:
            "academy", "genres", "films", "people", "public_response", "box_office".
        cache (bool, optional): Whether to cache the dataset for subsequent calls. Defaults to True.
        data_home (Optional[str], optional): The directory where dataset CSV files are stored.
            If None, uses the default data directory relative to the package. Defaults to None.
        as_frame (bool, optional): If True, returns the dataset as a pandas DataFrame.
            If False, returns the data as a NumPy array. Defaults to True.

    Returns:
        Union[pd.DataFrame, np.ndarray]: The loaded dataset.

    Raises:
        ValueError: If the provided dataset name is not recognized.
        FileNotFoundError: If the dataset CSV file is not found.
    """
    name_lower = name.lower()
    if name_lower not in _DATASETS:
        available = ", ".join(_DATASETS.keys())
        raise ValueError(
            f"Dataset '{name}' is not available. Available datasets are: {available}."
        )

    if cache and name_lower in _CACHE:
        data = _CACHE[name_lower]
    else:
        default_data_home = Path(data_home) if data_home else _get_default_data_home()
        file_path = default_data_home / _DATASETS[name_lower]
        if not file_path.exists():
            raise FileNotFoundError(f"Dataset file '{file_path}' not found.")
        data = pd.read_csv(file_path)
        if cache:
            _CACHE[name_lower] = data

    return data if as_frame else data.to_numpy()


def load_academy(
    cache: bool = True, data_home: Optional[str] = None, as_frame: bool = True
) -> Union[pd.DataFrame, np.ndarray]:
    """Load the Academy Awards dataset.

    Args:
        cache (bool, optional): Whether to cache the dataset. Defaults to True.
        data_home (Optional[str], optional): The directory where dataset CSV files are stored. 
                                             Defaults to None.
        as_frame (bool, optional): If True, returns the dataset as a pandas DataFrame;
            if False, as a NumPy array. Defaults to True.

    Returns:
        Union[pd.DataFrame, np.ndarray]: The Academy Awards dataset.
    """
    return load_dataset("academy", cache=cache, data_home=data_home, as_frame=as_frame)


def load_genres(
    cache: bool = True, data_home: Optional[str] = None, as_frame: bool = True
) -> Union[pd.DataFrame, np.ndarray]:
    """Load the Genres dataset.

    Args:
        cache (bool, optional): Whether to cache the dataset. Defaults to True.
        data_home (Optional[str], optional): The directory where dataset CSV files are stored. 
                                             Defaults to None.
        as_frame (bool, optional): If True, returns the dataset as a pandas DataFrame;
            if False, as a NumPy array. Defaults to True.

    Returns:
        Union[pd.DataFrame, np.ndarray]: The Genres dataset.
    """
    return load_dataset("genres", cache=cache, data_home=data_home, as_frame=as_frame)


def load_films(
    cache: bool = True, data_home: Optional[str] = None, as_frame: bool = True
) -> Union[pd.DataFrame, np.ndarray]:
    """Load the Pixar Films dataset.

    Args:
        cache (bool, optional): Whether to cache the dataset. Defaults to True.
        data_home (Optional[str], optional): The directory where dataset CSV files are stored. 
                                             Defaults to None.
        as_frame (bool, optional): If True, returns the dataset as a pandas DataFrame;
            if False, as a NumPy array. Defaults to True.

    Returns:
        Union[pd.DataFrame, np.ndarray]: The Pixar Films dataset.
    """
    return load_dataset("films", cache=cache, data_home=data_home, as_frame=as_frame)


def load_people(
    cache: bool = True, data_home: Optional[str] = None, as_frame: bool = True
) -> Union[pd.DataFrame, np.ndarray]:
    """Load the Pixar People dataset.

    Args:
        cache (bool, optional): Whether to cache the dataset. Defaults to True.
        data_home (Optional[str], optional): The directory where dataset CSV files are stored. 
                                             Defaults to None.
        as_frame (bool, optional): If True, returns the dataset as a pandas DataFrame;
            if False, as a NumPy array. Defaults to True.

    Returns:
        Union[pd.DataFrame, np.ndarray]: The Pixar People dataset.
    """
    return load_dataset("people", cache=cache, data_home=data_home, as_frame=as_frame)


def load_public_response(
    cache: bool = True, data_home: Optional[str] = None, as_frame: bool = True
) -> Union[pd.DataFrame, np.ndarray]:
    """Load the Public Response dataset.

    Args:
        cache (bool, optional): Whether to cache the dataset. Defaults to True.
        data_home (Optional[str], optional): The directory where dataset CSV files are stored. 
                                             Defaults to None.
        as_frame (bool, optional): If True, returns the dataset as a pandas DataFrame;
            if False, as a NumPy array. Defaults to True.

    Returns:
        Union[pd.DataFrame, np.ndarray]: The Public Response dataset.
    """
    return load_dataset(
        "public_response", cache=cache, data_home=data_home, as_frame=as_frame
    )


def load_box_office(
    cache: bool = True, data_home: Optional[str] = None, as_frame: bool = True
) -> Union[pd.DataFrame, np.ndarray]:
    """Load the Box Office dataset.

    Args:
        cache (bool, optional): Whether to cache the dataset. Defaults to True.
        data_home (Optional[str], optional): The directory where dataset CSV files are stored. 
                                             Defaults to None.
        as_frame (bool, optional): If True, returns the dataset as a pandas DataFrame;
            if False, as a NumPy array. Defaults to True.

    Returns:
        Union[pd.DataFrame, np.ndarray]: The Box Office dataset.
    """
    return load_dataset(
        "box_office", cache=cache, data_home=data_home, as_frame=as_frame
    )
