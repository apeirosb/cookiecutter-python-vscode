#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setup(
    name="{{ cookiecutter.project_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: {{ cookiecutter.open_source_license }}",
        "Operating System :: OS Independent",
    ],
    python_requires=">={{ cookiecutter.python_version }}",
    install_requires=requirements,
)
