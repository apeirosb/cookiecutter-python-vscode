# cookiecutter-python-vscode

Cookiecutter template for Python projects in Visual Studio Code.

## Features
- Linting: **flake8**
- Formatting: **black**
- Testing: **pytest**
- Code coverage: **coverage**
- Types annotations: **pyannotate**
- Type checker: **mypy**
- Imports sorting: **isort**
- Unused imports removal: **autoflake**
- **pre-commit**
- Settings and some useful extensions for **vscode**
- Virtual environment: **venv**
- **Dockerfile** (python:X.X-alpine image)
- Python package (**setup.py** and **conda**)

## Usage
Install cookiecutter:
```sh
pip install -U cookiecutter
```
Generate the project template:
```sh
cookiecutter gh:apeirosb/cookiecutter-python-vscode
```
Alternatively, if this repo has been cloned locally:
```sh
cookiecutter <path>/cookiecutter-python-vscode
```

In both cases, the Python project will be generated in the current directory.

## 3rd parties
- .gitignore taken from https://github.com/github/gitignore (Python.gitignore)
