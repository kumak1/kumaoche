from setuptools import setup, find_packages

setup(
    name='kumaoche',
    version='0.1.0',
    description='Pythonic Dev Repository & Dev Environment Management tool.',
    long_description='',
    author='kumak1',
    author_email='kumaki0@gmail.com',
    install_requires=['invoke'],
    url='https://github.com/kumak1/kumaoche',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
