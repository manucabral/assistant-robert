from setuptools import setup

with open('requirements.txt') as file:
    requirements = file.read().split('\n')

with open('README.md', 'r') as file:
    long_description = file.read()

VERSION = '0.0.3'
DESCRIPTION = 'A simple Python library that provides search with different search engines and more.'

setup(
    name = 'assistant-robert',
    author = 'Manuel Cabral',
    author_email = 'cabral.manuel@yandex.com',
    version = VERSION,
    description = DESCRIPTION,
    license = 'MIT',
    url = 'https://github.com/manucabral/assistant-robert',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['robert'],
    python_requires = '>= 3.9',
    install_requires = requirements,
    keywords = ['python', 'searcher', 'googlesearch', 'duckduckgosearch','html'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)