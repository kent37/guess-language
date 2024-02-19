#!/usr/bin/env python

import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="guess-language",
    version="0.2",
    description="Guess the natural language of a text",
    license="LGPL",
    platforms=["any"],
    author="Kent Johnson",
    author_email="kent3737@gmail.com",
    url="http://code.google.com/p/guess-language",
    packages=["guess_language"],
    package_data={
        "guess_language": [
            "trigrams/*",
            "Blocks.txt",
        ]
    },
    long_description=read("README"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.0",
)
