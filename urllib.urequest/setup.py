import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

setup(name='micropython-urllib.urequest',
      version='0.6.2',
      description='urllib.urequest module for MicroPython',
      long_description=open('README.rst').read(),
      url='https://github.com/pfalcon/micropython-lib',
      author='Paul Sokolovsky',
      author_email='micropython-lib@googlegroups.com',
      maintainer='Paul Sokolovsky',
      maintainer_email='micropython-lib@googlegroups.com',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      packages=['urllib'])
