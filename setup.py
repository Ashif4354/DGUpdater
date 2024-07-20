from setuptools import setup, find_packages

setup(
    name="dgupdater",
    version="0.0.1",
    author="DarkGlance",
    author_email="darkglance.developer@gmail.com",
    description="A CLI app updation assistant tool for python applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ashif4354/dgupdater",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.6',
    install_requires=[
        "click>=7.0",
    ],
    entry_points={
        'console_scripts': [
            'dgupdater=dgupdater.dgupdater:cli',
        ],
    },
)
