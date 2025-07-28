from setuptools import find_packages, setup

setup(
    name="text_normalizer",
    version="0.1.0",
    author="Hossein Khalilian",
    author_email="hsekhalilian@gmail.com",
    description="A lightweight Python package for text normalization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hossein-khalilian/text-normalizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],  # No external dependencies
)
