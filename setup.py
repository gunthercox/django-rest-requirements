#!/usr/bin/env python
"""
Django REST Requirements setup file.
"""
from setuptools import setup, find_packages


with open('requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='django-rest-requirements',
    version='1.0.1',
    url='https://github.com/gunthercox/django-rest-requirements',
    description='Django REST Requirements',
    author='Gunther Cox',
    author_email='gunthercx@gmail.com',
    install_requires=REQUIREMENTS,
    include_package_data=False,
    packages=find_packages(),
    package_dir={
        'django_rest_requirements': 'django_rest_requirements'
    },
    license='MIT',
    zip_safe=True,
    platforms=['any'],
    keywords=['django', 'rest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests'
)
