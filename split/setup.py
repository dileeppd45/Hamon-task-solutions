from setuptools import setup, find_packages

setup(
    name='splitter',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'splitter=splitter.split:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple utility for splitting items based on ratios',
    url='https://github.com/yourusername/splitter',
)