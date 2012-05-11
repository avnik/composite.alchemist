__version__ = '0.0'

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'zope.sqlalchemy',
    ]
test_requires = requires

setup(name='composite.alchemist',
      version=__version__,
      description='My own SQLAlchemy adapter for pyramid',
      long_description=README + '\n\nCHANGES\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      keywords='pyramid sqlalchemy',
      author="Alexander V. Nikolaev",
      author_email="avn@avnik.info",
      url="http://github.com/avnik/composite.alchemist",
      license="BSD-derived",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = requires,
      install_requires = test_requires,
      test_suite="composite.alchemist.test",
      extras_require = {
          'test': test_requires,
          'zcml': [
              'zope.schema',
              'pyramid_zcml',
              ]
          }
      )

