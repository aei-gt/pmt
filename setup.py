from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pmt/__init__.py
from pmt import __version__ as version

setup(
	name="pmt",
	version=version,
	description="Gestion de Movilidad y Transito",
	author="aei.gt",
	author_email="info@aei.gt",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
