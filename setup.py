from setuptools import setup, find_packages
from theHarvester.lib.core import Core

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='theHarvester',
    version=Core.version(),
    author="Christian Martorella",
    author_email="cmartorella@edge-security.com",
    description="theHarvester is a very simple, yet effective tool designed to be used in the early stages of a penetration test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laramies/theHarvester",
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.7',
    scripts=['bin/theHarvester'],
    install_requires=[
        "aiodns==2.0.0",
        "aiohttp==3.6.3",
        "aiomultiprocess==0.8.0",
        "aiosqlite==0.15.0",
        "beautifulsoup4==4.9.3",
        "certifi==2020.6.20",
        "dnspython==2.0.0",
        "netaddr==0.8.0",
        "plotly==4.11.0",
        "pyppeteer==0.2.2",
        "PyYAML==5.3.1",
        "requests==2.24.0",
        "retrying==1.3.3",
        "shodan==1.24.0",
        "texttable==1.6.3",
        "lxml==4.6.1",
        "uvloop==0.14.0; platform_system != 'Windows'",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    data_files=[
        ('/etc/theHarvester', [
            'wordlists/general/common.txt',
            'wordlists/dns-big.txt',
            'wordlists/dns-names.txt',
            'wordlists/dorks.txt',
            'wordlists/names_small.txt',
            'api-keys.yaml',
            'proxies.yaml'
        ]
        )
    ],
)
