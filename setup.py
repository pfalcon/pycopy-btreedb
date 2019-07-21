from setuptools import setup
import sdist_upip


setup(name='pycopy-btreedb',
      version='0.4',
      description="""Very simple ORM (Object-Relational \
Mapper) for Pycopy's 'btree' module.
""",
      url='https://github.com/pfalcon/pycopy-btreedb',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      py_modules=['btreedb'])
