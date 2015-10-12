from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='JpTokenPreprocessing',
    version='0.1.5a2',
    description='JpTokenPreprocessing is Python library for token preprocessing.',
    long_description=long_description,
    url='https://github.com/Kesin11/JpTokenPreprocessing',
    download_url='https://github.com/Kesin11/JpTokenPreprocessing/archive/master.zip',
    author='Kenta Kase',
    author_email='kesin1202000@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Operating System Kernels :: Linux',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Natural Language :: Japanese',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='NLP, natural language processing, token, japaneese',
)
