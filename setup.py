try:
    # Use setuptools if available, for install_requires (among other things).
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Pylsy',
    packages=['pylsy'],
    version="1.003",
    description='A simple Python library for easily displaying tabular data ina visually appealing ASCII table format',
    url='https://github.com/Leviathan1995/Pylsy',
)
