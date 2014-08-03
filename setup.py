from setuptools import setup, find_packages

print find_packages()

setup(
    name = 'Robot Framework ServerSpec 2 Library',
    version = '0.1',
    description = 'Server spec on Robot Framework inspired from Serverspec on Ruby',    packages = find_packages(),
    keywords = 'serverspec robotframework robot',
    author = 'Thanabodee Charoenpiriyakij',
    author_email = 'wingyminus@gmail.com',
    install_requires = ['robotframework>=2.8.5', 'paramiko>=1.14.0'],
    package_dir = {'': 'src'},
    packages = find_packages(),
)
