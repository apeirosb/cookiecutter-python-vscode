#!/bin/bash

# Init git repo
git init

# Virtual environment
{% if cookiecutter.environment == "venv" %}
python{{ cookiecutter.python_version }} -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
versioneer install
pre-commit install
{% endif %}

# Cleanup
{% if cookiecutter.add_conda_build != "yes" %} rm -rf conda-recipe {% endif %}
{% if cookiecutter.add_vscode_settings != "yes" %} rm -rf .vscode {% endif %}
{% if cookiecutter.environment != "Dockerfile" %} rm -f Dockerfile & rm -rf .devcontainer {% endif %}
