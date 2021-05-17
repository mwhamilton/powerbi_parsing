from distutils.core import setup
import setuptools
import os


setuptools.setup(
    name='powerbi_parser',
    version='0.0.1',
    author='Matthew Hamilton',
    author_email='mwhamilton6@gmail.com',
    description="A package to handle powerbi parsing",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    dependencies=[],
    include_package_data=True,
)