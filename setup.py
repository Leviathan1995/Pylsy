try:
    # Use setuptools if available, for install_requires (among other things).
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Pylsy',
    packages=['pylsy'],
    version="1.003",
    description='Pylsy is a simple Python library draw tables in the Terminal.Just tow lines of code',
    url='https://github.com/Leviathan1995/Pylsy',
)
