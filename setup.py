"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['myclient.pyw']
DATA_FILES = ['ATone.mp3','Blop.mp3','transparent.png']
OPTIONS = {
    'iconfile': 'kokota.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
