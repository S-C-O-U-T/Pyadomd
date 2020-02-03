from distutils.core import setup
setup(
  name = 'pyadomd',         # How you named your package folder (MyLib)
  packages = ['pyadomd'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='Apache License 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A pythonic approach to query SSAS data models',   # Give a short description about your library
  author = 'SCOUT',                   # Type in your name
  author_email = 'andboye@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/Andboye/Pyadomd',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Andboye/Pyadomd/archive/v_0.0.1.tar.gz', 
  keywords = ['adomd', 'ssas', 'ssas-tabular', 'ssasadomd'],   # Keywords that define your package best
  install_requires=[            
          'pythonnet'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',   # Again, pick a license 
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)