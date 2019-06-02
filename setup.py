import codecs
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='pyautodoc',
    version='0.6.3',
    packages=find_packages(),
    url='https://github.com/alvarogf97/pyautodoc',
    license='MIT',
    author='Alvaro',
    author_email='alvarogf97@gmail.com',
    install_requires=[
        'sphinx',
        'm2r',
        'pyyaml'
    ],
    classifiers=[],
    long_description=readme(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'pyautodoc = pyautodoc.scripts.main:main'
        ]
    },
    python_requires=">=3.4",
)
