# pip install setuptools

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
