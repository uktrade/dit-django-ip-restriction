import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ip_safelist',
    version=0.1,
    packages=find_packages(),
    include_package_data=True,
    license='',
    description='IP safelisting tools to restrict access to the django admin or the entire site',
    long_description=README,
    url='https://gov.uk/',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'django',
        'django-basicauth==0.5.1',
    ]
)
