"""
Flask-Role-Required
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-Role-Required',
    version='0.1',
    url='',
    license='',
    author='Janne Jokinen',
    author_email='jokinen.p.janne@gmail.com',
    description='',
    long_description=__doc__,
    py_modules=['flask_role_required.py'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)