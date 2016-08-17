from setuptools import setup, find_packages

setup(
    name = 'robotframework-serverspeclibrary',
    version = '0.2',
    description = 'Server spec on Robot Framework inspired from Serverspec on Ruby',
    url = 'https://github.com/wingyplus/robotframework-serverspeclibrary',
    keywords = 'serverspec robotframework robot',
    license = 'MIT',
    author = 'Thanabodee Charoenpiriyakij',
    author_email = 'wingyminus@gmail.com',
    install_requires = ['robotframework>=2.8.5', 'paramiko>=1.14.0'],
    package_dir = {'': 'src'},
    packages = ['ServerSpecLibrary', 'ServerSpecLibrary.keywords']
)
