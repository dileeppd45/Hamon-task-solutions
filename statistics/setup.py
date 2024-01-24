from setuptools import setup, find_packages


setup(
    name='unemployment_statistics',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your project may have
    ],
    entry_points={
        'console_scripts': [
            'calculate_statistics=statistics.statistics:main',
        ],
    },
)