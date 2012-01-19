from setuptools import setup, find_packages
import os

version = '1.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='js.lavalamp',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='fanstatic lavalamp',
      author='Petri Savolainen',
      author_email='petri.savolainen@koodaamo.fi',
      url='https://github.com/koodaamo/js.lavalamp',
      license='GPL',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'fanstatic',
          'js.jquery',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
          [fanstatic.libraries]
          js_lavalamp = js.lavalamp:library
          # -*- Entry points: -*-
      """,
      )
