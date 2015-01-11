import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.org')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='passwordsafe',
    version='0.1',
    packages=['passwordsafe'],
    include_package_data=True,
    license='AGPL-3',
    description='Web-based credentials management application with RESTful API and LDAP integration',
    long_description=README,
    url='https://github.com/treytabner/passwordsafe',
    author='Trey Tabner',
    author_email='trey@tabner.com',
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: AGPL-3',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
