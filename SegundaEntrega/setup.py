
# Comandos desde la terminal:

# pip install setuptools
# python -m pip install setuptools

# linux o mac
# pip3 install setuptools
# python3 -m pip install setuptools

# python setup.py sdist
from setuptools import setup  # , find_packages

setup(
    name="Modelo_Cliente_Del_Valle",
    version="0.1",
    description="Segunda entrega del curso de Python",
    author="Eduardo del Valle",
    author_email="eduardodelvalle_90@hotmail.com",
    packages=["Clases"],
)
