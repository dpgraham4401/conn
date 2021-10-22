"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
from setuptools import setup
setup(
    name='conn',
    entry_points={
        'console_scripts': [
            'conn = conn:main',
        ],
    }
)
