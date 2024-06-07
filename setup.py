from pathlib import Path

from setuptools import find_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

docs_packages = ["mkdocs", "mkdocstrings"]

style_packages = ["black", "flake8", "isort"]

dev_packages = ["pip-tools", "pandas", "pytest", "pytest-asyncio", "pytest-mock"]

# Define our package
setup(
    name="CV_Promoter",
    version=0.1,
    description="This application uses LLMs to extract data from a CV and populate a form from that information.",
    author="Ryan Godwin",
    author_email="ryangodwin@uabmc.edu",
    url="https://gitlab.rc.uab.edu/anes_ai/llm_apps/cv_promoter",
    python_requires=">=3.10",
    packages=find_packages(),  # only look in directores with __init__.py
    install_requires=[required_packages],
    extras_require={"dev": docs_packages + style_packages + dev_packages, "docs": docs_packages},
)
