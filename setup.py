"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup
import os, pygame

pygamedir = os.path.split(pygame.base.__file__)[0]

NAME = 'bomerman'
VERSION = '0.1'

plist = dict(
    CFBundleIconFile=NAME,
    CFBundleName=NAME,
    CFBundleShortVersionString=VERSION,
    CFBundleGetInfoString=' '.join([NAME, VERSION]),
    CFBundleExecutable=NAME,
    CFBundleIdentifier='org.pygame.ricky.bomberman',
)

setup(
    data_files=['resources', 'Net',os.path.join(pygamedir, pygame.font.get_default_font()),
		],
    app=[
        dict(script="main.py", plist=plist),
    ],
    setup_requires=["py2app"],
)
