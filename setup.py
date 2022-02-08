#!/usr/bin/python

import pathlib
import sys

import setuptools

# Get root directory.
root_dir = pathlib.Path(__file__).parent.resolve()

# Add root directory to PYTHONPATH.
sys.path.insert(0, root_dir)

# Get source directory.
src_dir = root_dir / "foo"

# Find packages within source directory.
packages = setuptools.find_packages(where=str(src_dir))

# Read dependencies for documentation generation.
docs_requirements_file = root_dir / "docs" / "requirements.txt"
docs_requirements = docs_requirements_file.read_text().splitlines()

setuptools.setup(
    name="foo",
    version="0.0.9",
    description="A Python package test2",
    long_description="",
    url="",
    author="",
    author_email="",
    license="MIT",
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    # https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point
    # https://click.palletsprojects.com/en/7.x/setuptools/
    # entry_points={"console_scripts": ["foo=foo.__main__:cli"]},
    install_requires=["numpy>=1.20", "click"],
    extras_require={
        # "test": ["pytest", "coverage"],
        # "lint": ["pylama", "isort", "mypy"],
        "docs": docs_requirements,
    },
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
