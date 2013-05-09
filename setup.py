# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = open('version.txt').read().strip()

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='cyplp.timelapsetaker',
      version=version,
      description="application for timelapse",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='template',
      author=u'Cyprien Le Pannérer',
      author_email='clepannerer@edd.fr',
      url='',
      packages=find_packages(),
      namespace_packages=['cyplp'],
      include_package_data=True,
      package_data={'cyplp.timelapsetaler': ['README.txt', 'CHANGES.txt', 'MANIFEST.in']},
      zip_safe=False,
      install_requires=[
          'setuptools',
          'cyplp.gphoto2',
          'pyzmq',
          'couchdbkit',
          'pyramid',

          # -*- Extra requirements: -*-
      ],
      entry_points={
	  'console_scripts': [
	      'timelapse = cyplp.timelapsetaker:main',
          ],
      },
      )
