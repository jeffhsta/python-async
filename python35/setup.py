from setuptools import setup


setup(name='asyncapp',
      version='0.1',
      description='Simple async app in Python 3.5',
      author='Jeff Stachelski',
      author_email='jeffhsta@riseup.net',
      url='https://github.com/jeffhsta/python-async',
      packages=[ 'asyncapp' ],
      install_requires=[],
      entry_points={
          'console_scripts': [
              'asyncapp = main:main'
          ]
      },
      include_package_data=True)
