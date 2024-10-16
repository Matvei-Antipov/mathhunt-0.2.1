from setuptools import setup, find_packages

setup(
    name="mathhunt",
    version="0.1.0",
    author="Matvei Antipov",
    author_email="matveiantipov2007@gmail.com",
    description="Toolkit for math calculations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matvei-Antipov/mathhunt-0.1.0.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)