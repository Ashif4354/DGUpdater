from setuptools import setup, find_packages

setup(
    name="dgupdater",
    version="1.0.3",
    author="DarkGlance",
    author_email="darkglance.developer@gmail.com",
    description="A NO/LOW Code CLI based auto updation assistant tool for python applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6',
    install_requires=[
        "click>=7.0",
        "pymongo",
        "platformdirs",
        "tqdm",
        "rich"

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
        'cli tool', 'python', 'pyupdater',
        'python application', 'auto updation', 
        'auto update', 'update',
        'cli', 'command line interface'
        'no code', 'low code', 'no code tool',
        'mongodb', 'pymongo', 'click'
    ]
)
