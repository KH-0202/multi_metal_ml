from setuptools import setup, find_packages

setup(
    name="multi_metal_ml",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
	"multi_metal_ml": ["data/time_temp_data/*.csv", "data/time_temp_data_validate/*.csv"],
    },
    install_requires=[
        "numpy",
        "pandas",
        "tensorflow",
        "scikit-learn",
        "matplotlib"
    ],
    author="Kassandra Hernandez",
    author_email="hernkass@oregonstate.edu",
    description="A machine learning package for multi-metal additive manufacturing",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
