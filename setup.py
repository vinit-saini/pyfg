import uuid

from setuptools import setup, find_packages

with open("requirements.txt") as file:
    reqs = [
        line for line in file
        if line.strip() and not line.lstrip().startswith(("#", "git+"))
    ]

setup(
    name="pyfg",
    version="0.50",
    packages=find_packages(),
    author="XNET",
    author_email="lindblom+pyfg@spotify.com",
    description="Python API for fortigate",
    url="https://github.com/spotify/pyfg",
    include_package_data=True,
    install_requires=reqs
)
