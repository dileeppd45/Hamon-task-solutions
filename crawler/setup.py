from setuptools import setup, find_packages

setup(
    name='crawler',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'crawler=crawler.crawler:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
        'beautifulsoup4==4.12.3',
        'certifi==2023.11.17',
        'charset-normalizer==3.3.2',
        'idna==3.6',
        'requests==2.31.0',
        'urllib3==2.1.0'
    ],
    author='DILEEP',
    author_email='dileeppd45@gmail.com',
    description='The function will scrape the website https://www.gettyimages.in/photos/aamir-khan-actor and download all 60 images from the website.',
    url='https://github.com/yourusername/crawler',
)