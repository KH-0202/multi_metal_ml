# Multi-Metal Machine Learning (multi_metal_ml)

## Overview
This package applies machine learning to optimize multi-metal additive manufacturing processes.

## Features
- Train models using thermal history data in the form of .csv files.
- Predict microstructure evolution.
- Support for user-defined microstructure phases.

## Installation
Clone the repository, create a virtual environment, and install dependencies:
```bash
git clone https://github.com/yourusername/multi_metal_ml.git
cd multi_metal_ml
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Example
How to run an example (requires .csv files):
```bash
pip install -e .
python examples/example_run.py
```

## Testing suite
How to run testing suite
```bash
cd tests
pytest
```

## License
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
