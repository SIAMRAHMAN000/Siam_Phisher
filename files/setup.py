#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='Siam_Phisher',
    version=version,
    description='A python phishing script for login phishing, image phishing video phishing an many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Siam Rahman',
    author_email='s14mbro1@gmail.com',
    license="MIT",
    scripts=['siamphisher'],
    install_requires=["requests", "bs4", "rich"]
)
