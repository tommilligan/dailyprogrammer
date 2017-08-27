#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="dailyprogrammer",
    version="0.0.1",
    license="Apache License 2.0",
    url="https://github.com/tommilligan/dailyprogrammer/",
    author="Tom Milligan",
    author_email="code@tommilligan.net",
    description="Working solutions to https://www.reddit.com/r/dailyprogrammer",
    keywords="daily challenge programmer reddit",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    zip_safe=False,
    platforms="any",
    install_requires=[
        "six",
    ],
    tests_require=[
        "nose2"
    ],
    test_suite="nose2.collector.collector",
    entry_points={
        "console_scripts": [
            "dailyprogrammer = dailyprogrammer.__main__:main"
        ]
    },
)