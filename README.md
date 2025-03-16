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

## Citation
@Article{         harris2020array,
 title         = {Array programming with {NumPy}},
 author        = {Charles R. Harris and K. Jarrod Millman and St{\'{e}}fan J.
                 van der Walt and Ralf Gommers and Pauli Virtanen and David
                 Cournapeau and Eric Wieser and Julian Taylor and Sebastian
                 Berg and Nathaniel J. Smith and Robert Kern and Matti Picus
                 and Stephan Hoyer and Marten H. van Kerkwijk and Matthew
                 Brett and Allan Haldane and Jaime Fern{\'{a}}ndez del
                 R{\'{i}}o and Mark Wiebe and Pearu Peterson and Pierre
                 G{\'{e}}rard-Marchant and Kevin Sheppard and Tyler Reddy and
                 Warren Weckesser and Hameer Abbasi and Christoph Gohlke and
                 Travis E. Oliphant},
 year          = {2020},
 month         = sep,
 journal       = {Nature},
 volume        = {585},
 number        = {7825},
 pages         = {357--362},
 doi           = {10.1038/s41586-020-2649-2},
 publisher     = {Springer Science and Business Media {LLC}},
 url           = {https://doi.org/10.1038/s41586-020-2649-2}
}

@software{reback2020pandas,
    author = {The pandas development team},
    title = {pandas-dev/pandas: Pandas},
    month = feb,
    year = 2020,
    publisher = {Zenodo},
    version = {<2.2.3>},
    doi = {10.5281/zenodo.<insert DOI number>},
    url = {https://doi.org/10.5281/zenodo.<insert DOI number>}
}

@misc{tensorflow2015-whitepaper,
title={ {TensorFlow}: Large-Scale Machine Learning on Heterogeneous Systems},
url={https://www.tensorflow.org/},
note={Software available from tensorflow.org},
author={
    Mart\'{i}n~Abadi and
    Ashish~Agarwal and
    Paul~Barham and
    Eugene~Brevdo and
    Zhifeng~Chen and
    Craig~Citro and
    Greg~S.~Corrado and
    Andy~Davis and
    Jeffrey~Dean and
    Matthieu~Devin and
    Sanjay~Ghemawat and
    Ian~Goodfellow and
    Andrew~Harp and
    Geoffrey~Irving and
    Michael~Isard and
    Yangqing Jia and
    Rafal~Jozefowicz and
    Lukasz~Kaiser and
    Manjunath~Kudlur and
    Josh~Levenberg and
    Dandelion~Man\'{e} and
    Rajat~Monga and
    Sherry~Moore and
    Derek~Murray and
    Chris~Olah and
    Mike~Schuster and
    Jonathon~Shlens and
    Benoit~Steiner and
    Ilya~Sutskever and
    Kunal~Talwar and
    Paul~Tucker and
    Vincent~Vanhoucke and
    Vijay~Vasudevan and
    Fernanda~Vi\'{e}gas and
    Oriol~Vinyals and
    Pete~Warden and
    Martin~Wattenberg and
    Martin~Wicke and
    Yuan~Yu and
    Xiaoqiang~Zheng},
  year={2015},
}

@article{pedregosa2011scikit,
  title={Scikit-learn: Machine learning in Python},
  author={Pedregosa, Fabian and Varoquaux, Ga{\"e}l and Gramfort, Alexandre and Michel, Vincent and Thirion, Bertrand and Grisel, Olivier and Blondel, Mathieu and Prettenhofer, Peter and Weiss, Ron and Dubourg, Vincent and others},
  journal={Journal of machine learning research},
  volume={12},
  number={Oct},
  pages={2825--2830},
  year={2011}
}

@Article{Hunter:2007,
  Author    = {Hunter, J. D.},
  Title     = {Matplotlib: A 2D graphics environment},
  Journal   = {Computing in Science \& Engineering},
  Volume    = {9},
  Number    = {3},
  Pages     = {90--95},
  abstract  = {Matplotlib is a 2D graphics package used for Python for
  application development, interactive scripting, and publication-quality
  image generation across user interfaces and operating systems.},
  publisher = {IEEE COMPUTER SOC},
  doi       = {10.1109/MCSE.2007.55},
  year      = 2007
}

@misc{pytest 8.3.5,
  title =        {pytest 8.3.5},
  author = {Krekel, Holger and Oliveira, Bruno and Pfannschmidt, Ronny and Bruynooghe, Floris and Laugher, Brianna and Bruhin, Florian},
  year =         {2004},
  url = {https://github.com/pytest-dev/pytest},
}
