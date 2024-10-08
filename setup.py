from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in library_managment/__init__.py
from library_managment import __version__ as version

setup(
	name="library_managment",
	version=version,
	description="lib mange system",
	author="yalhaj",
	author_email="y@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
