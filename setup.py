from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'pyadomd',         # How you named your package folder (MyLib)
  packages = ['pyadomd'],   # Chose the same as "name"
  version = '0.0.8',      # Start with a small number and increase it with every change you make
  license='Apache License 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A pythonic approach to query SSAS data models',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'SCOUT',                   # Type in your name
  author_email = 'andboy@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Andboye/Pyadomd',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Andboye/Pyadomd/archive/v0.0.8.tar.gz', 
  keywords = ['adomd', 'ssas', 'ssas-tabular', 'ssasadomd'],   # Keywords that define your package best
  install_requires=[            
          'pythonnet'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Database',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)