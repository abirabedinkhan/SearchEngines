from setuptools import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name             = 'SearchEngines',
    version          = '0.0.1',
    description      = 'SearchEngines is a package that contains all the search engines to get the results from them',
    author           = 'Abir Abedin Khan',
    author_email     = 'abirabedinkhan@yahoo.com',
    url              = 'https://github.com/abirabedinkhan/SearchEngines',
    packages         = find_packages(exclude=('test*')),
    install_requires = requirements,
    license          = 'MIT'
)