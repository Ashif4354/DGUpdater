from setuptools import setup, find_packages
# print(find_packages())

setup(
    name="dgupdater",
    version="0.3.2",
    author="DarkGlance",
    author_email="darkglance.developer@gmail.com",
    description="A CLI based auto updation assistant tool for python applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 2 - Pre-Alpha',
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Utilities'
    ],
    python_requires='>=3.6',
    install_requires=[
        "click>=7.0",
        "pymongo",
        "platformdirs"

    ],
    entry_points={
        'console_scripts': [
            'dgupdater=dgupdater:cli',
        ],
    },
    project_urls = {
        'Github': "https://github.com/Ashif4354/dgupdater"
    },
    keywords= [
        'dgupdater', 'auto updater', 
        'cli tool', 'python', 
        'python application', 'auto updation', 
        'auto update', 'update',
        'cli', 'command line interface'
        'no code', 'low code', 'no code tool',
        'mongodb', 'pymongo', 'click', 
        'darkglance', 'darkglance developer',
        'ashif', 'pypi', 'pip',
    ]
)
