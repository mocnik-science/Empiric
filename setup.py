from setuptools import setup
import setuptools

setup(
  name=libName,
  packages=['Empiric', 'Empiric.internal'],
  install_requires=[
    'flask',
  ],
  version=libVersion,
  author='Franz-Benjamin Mocnik',
  author_email='mail@mocnik-science.net',
  description='Empiric, the flexible framework for conducting empirical experiments',
  license='GPL-3',
  url=libUrl,
  download_url='',
  keywords=['empirical experiment', 'map', 'framework', 'testing', 'psychology', 'cognition'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3',
  ],
  python_requires='>=3.6',
)
