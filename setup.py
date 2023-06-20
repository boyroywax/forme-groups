from setuptools import setup, find_packages

setup(
    name='groups',
    version='0.0.1',
    description='A package for managing groups of decentralized objects',
    author='Forme Technologies',
    url='https://github.com/formesbs/forme-groups',
    packages=find_packages('', 'src/groups/'),
    install_requires=[
        # list your dependencies here
    ]
)
