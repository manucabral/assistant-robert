from setuptools import setup

with open('requirements.txt') as file:
    requirements = file.read().split('\n')

with open('README.md', 'r') as file:
    long_description = file.read()

VERSION = '0.0.1'
DESCRIPTION = 'A Python web searcher library with different search engines.'

setup(
    name = 'robert-helper',
    author = 'Manuel Cabral',
    version = VERSION,
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['robert'],
    python_requires = '>= 3.9',
    install_requires = requirements,
    keywords = ['python', 'searcher', 'googlesearch', 'html'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)