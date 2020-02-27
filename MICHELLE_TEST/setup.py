from setuptools import setup, find_packages

setup(
    name='michelle_test',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/michelleb123za/michelle_test',
    author='Michelle',
    author_email='michelleb123za@gmail.com'
)