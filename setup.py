from distutils.core import setup

from setuptools import find_packages

setup(
    name="radio",
    version="1.0.0",
    packages=find_packages(exclude=["tests"]),
    url="https://konungstvo.ru",
    license="GPLv3",
    author="xunto",
    author_email="",
    description="",
    entry_points={
        "console_scripts": [
            "radio=radio.aiohttp_controller:run"
        ],
    },
    install_requires=[
        "aiohttp==3.1.3",
        "motor==1.2.1", 'shouty'
    ],
    extras_require={
        "dev": [
            "pytest==3.5.0",
            "pytest-asyncio==0.8.0"
        ]
    }
)
