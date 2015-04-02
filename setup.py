from setuptools import setup, find_packages
import os

version = '1.5.3'

setup(name='quintagroup.megamenu',
      version=version,
      description="Mega menu for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 3.2",
          "Framework :: Plone :: 3.3",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Operating System :: OS Independent",
          "Development Status :: 5 - Production/Stable",
      ],
      keywords='menu mega panels',
      author='Quintagroup',
      author_email='support@quintagroup.com',
      url='https://github.com/quintagroup/quintagroup.megamenu/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['quintagroup'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.panels',
          # -*- Extra requirements: -*-
      ],
      extras_require={'tests':['Products.PloneTestCase']},
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
