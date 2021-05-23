import setuptools
import powerbi_parser


setuptools.setup(
    name='powerbi_parser',
    version=powerbi_parser.__version__,
    author='Matthew Hamilton',
    author_email='mwhamilton6@gmail.com',
    description="A package to handle powerbi parsing",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    dependencies=[],
    include_package_data=True,
)