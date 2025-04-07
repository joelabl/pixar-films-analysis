# Pixar Films Analysis

This project uses Python for importing and analyzing Pixar films datasets. It provides also a simple package as an interface to load various datasets (e.g., Academy Awards, genres, films, people, public responses, and box office) for further analysis.

## Installation

Clone the repository, create a conda environment, and install the pixarfilms folder as a package using pip:
```bash
git clone https://github.com/joelabl/pixar-films-analysis.git
cd pixar-films-analysis
conda env create -f environment.yml
conda activate pixar_data_analysis
pip install -e .
```

## Usage
Download the datasets:
```bash
python examples/scripts/scrape_data.py
```

You can load datasets in two styles:<br>
**Sklearn Style**
```python
from pixarfilms.datasets import load_academy, load_genres

df_academy = load_academy(as_frame=True)
arr_genres = load_genres(as_frame=False)
```

**Seaborn Style**
```python
from pixarfilms import load_dataset

df_box_office = load_dataset("box_office", cache=True)
```

## License
This project is licensed under the MIT License.<br>
It includes data directly derived from [Eric Leung R package](https://github.com/erictleung/pixarfilms?tab=readme-ov-file#data).<br>
The datasets themselves are based on content from Wikipedia and OMDb, and are therefore licensed under **CC BY-SA 4.0**.