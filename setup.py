import re
import os
from pathlib import Path
from setuptools import setup


def find_version(filename):
    _version_re = re.compile(r"__version__ = '(.*)'")
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)


__version__ = find_version('sparcur/__init__.py')


def do_emacs_things():
    'emacs -q -batch -L . --no-site-file --load org --load ob-shell'
    ['emacs',
     '--batch',
     '--no-init-file',
     '--no-site-file',
     '--directory', '.',
     '--load', 'org',
     '--load', 'ob-shell',
     '--load', 'ob-python',
     '--eval', '(org-babel-tangle-file "docs/developer-guide.org")',
     ]


with open('README.md', 'rt') as f:
    long_description = f.read()

tests_require = ['pytest', 'pytest-runner']
setup(name='sparcur',
      version=__version__,
      description='assorted',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/tgbugs/sparc-curation',
      author='Tom Gillespie',
      author_email='tgbugs@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      keywords='SPARC curation biocuration ontology blackfynn protc protocols hypothesis',
      packages=['sparcur', 'sparcur.export'],
      python_requires='>=3.6',
      tests_require=tests_require,
      install_requires=[
          'augpathlib>=0.0.21',
          'beautifulsoup4',
          'blackfynn>=3.0.0',
          'dicttoxml',
          'idlib>=0.0.1.dev8',
          "ipython; python_version < '3.7'",
          'jsonschema>=3.0.1',  # need the draft 6 validator
          'ontquery>=0.2.7',
          'openpyxl',
          'protcur>=0.0.7',
          'pyontutils>=0.1.26',
          'pysercomb>=0.0.8',
          'rdflib_jsonld',
          'terminaltables',
          'xlsx2csv',
      ],
      extras_require={'dev': ['wheel'],
                      'filetypes': ['nibabel', 'pydicom', 'scipy'],
                      'test': tests_require},
      scripts=[],
      entry_points={
          'console_scripts': [
              'spc=sparcur.cli:main',
          ],
      },
      data_files=[]
     )
