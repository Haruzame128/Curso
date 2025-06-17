
# Comandos desde la terminal:

# pip install setuptools
# python -m pip install setuptools

# linux o mac
# pip3 install setuptools
# python3 -m pip install setuptools

# python setup.py sdist
from setuptools import setup  # , find_packages

setup(
    name="mi_primer_paquete",
    version="0.1",
    description="Mi primer paquete en Python",
    author="Migue",
    author_email="ejemplo@email.com",
    # packages=find_packages(),  # Busca automáticamente los paquetes
    packages=["mi_primer_paquete"],
)
