import setuptools

__author__ = 'Sobolev Andrey <email.asobolev@gmail.com>'
__version__ = '0.0.1.1'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hex-json',
    version=__version__,
    install_requires=['orjson>=3.8.6'],
    author='Sobolev Andrey',
    author_email='email.asobolev@gmail.com',
    description='Convert [Python dictionary | ASCII JSON string] into hexadecimal string.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Sobolev5/hex-json/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)