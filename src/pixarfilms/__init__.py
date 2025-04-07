"""Pixar Films package.

This package provides functions to import and analyze Pixar films datasets.
"""

from .datasets import (
    load_dataset,
    load_academy,
    load_genres,
    load_films,
    load_people,
    load_public_response,
    load_box_office,
)

__all__ = [
    "load_dataset",
    "load_academy",
    "load_genres",
    "load_films",
    "load_people",
    "load_public_response",
    "load_box_office",
]
