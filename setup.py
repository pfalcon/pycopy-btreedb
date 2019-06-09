from setuptools import setup
import sdist_upip


setup(name='micropython-btreedb',
      version='0.3.1',
      description="""Very simple, btree-based ORM (Object-Relational \
Mapper) for MicroPython.
""",
      url='https://github.com/pfalcon/micropython-btreedb',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      py_modules=['btreedb'])
