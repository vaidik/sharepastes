#!/usr/bin/env python
import platform

from setuptools import setup, find_packages

from sharepastes import __version__

deps = [
    'xerox==0.3.1',
    'pygithub3==0.5',
]

# install pync on mac
if platform.system() == 'Darwin':
    deps.append('pync==1.1')

setup(
    name='SharePastes',
    version=__version__,
    author='Vaidik Kapoor',
    author_email='kapoor.vaidik@gmail.com',
    description='A utility tool to help you share code snippets.',
    install_requires=deps,
    packages=['sharepastes'],
    entry_points={
        'console_scripts': [
            'sharepastes = sharepastes.runner:main'
        ]
    }
)
