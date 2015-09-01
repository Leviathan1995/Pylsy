try:
    # Use setuptools if available, for install_requires (among other things).
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Pylsy',
    packages=['pylsy'],
    version="1.003",
    description='Pylsy is a simple  library draw tables in the Terminal.',
    url='https://github.com/Leviathan1995/Pylsy',
)
