from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in idmshealtycare/__init__.py
from idmshealtycare import __version__ as version

setup(
	name="idmshealtycare",
	version=version,
	description="Sistem Informasi Rumah Sakit",
	author="PT IDMS",
	author_email="jeff.sidik@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
