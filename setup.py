from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_sandbox/__init__.py
from frappe_sandbox import __version__ as version

setup(
	name="frappe_sandbox",
	version=version,
	description="Frappe Sandbox",
	author="chillaranand",
	author_email="chillar@f.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
