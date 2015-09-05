try:
    # Use setuptools if available, for install_requires (among other things).
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Pylsy',
    packages=['pylsy'],
    version="1.2",
    description='Pylsy is a simple  library draw tables in the Terminal.',
    author='leviathan',
    author_email='leviathan1995@outlook.com',
    url='https://github.com/Leviathan1995/Pylsy',
    test_suite='pylsy.tests',
)
