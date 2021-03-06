from os.path import abspath, dirname, join
from setuptools import setup, find_packages

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='flight-optimizer',
    version='0.2.0',
    python_requires='>=3.6,<4.0',
    description='Package that searches for the cheapest airplane flights per kilometer.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Erik Duisheev',
    author_email='erik.duisheev@gmail.com',
    license='UNLICENSE',
    packages=find_packages(),
    install_requires=[
        'click==7.1.2',
        'pytest==5.4.3',
        'pytest-mock==3.1.1',
        'dataclasses==0.6',
        'requests==2.24.0',
        'haversine==2.2.0',
    ],
    entry_points={
        'console_scripts': [
            'flight_optimizer = flight_optimizer.cli:search'
        ],
    }
)
