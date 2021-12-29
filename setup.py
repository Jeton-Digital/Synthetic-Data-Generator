import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="synthetic-data-generator-pkg",
    version="0.0.2",
    author="Efe Buyuk",
    author_email="hello@jetondigital.com",
    description="Python package for generating synthetic data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jeton-Digital/Synthetic-Data-Generator",
    project_urls={
        "Bug Tracker": "https://github.com/Jeton-Digital/Synthetic-Data-Generator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "barnum",
        "Faker",
        "future",
        "names",
        "python-dateutil",
        "six",
        "text-unidecode",
    ],
)
