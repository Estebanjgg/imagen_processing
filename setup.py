from distutils.command import install
from gettext import find
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="Comparador de imagenes",
    version="0.0.1",
    author="Esteban Gonzalez",
    author_email="esteban030990@gmail.com",
    description=("Comparacion de imagenes."),
    long_description=page_description,
    long_description_content_type="text/markdown",           
    url="https://github.com/Estebanjgg/image_processing",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
   

)
