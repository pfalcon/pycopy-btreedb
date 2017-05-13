from setuptools import setup
import optimize_upip


setup(name='micropython-btreedb',
      version='0.2',
      description="""Very simple, btree-based ORM (Object-Relational
Mapper) for MicroPython.
""",
      url='https://github.com/pfalcon/micropython-btreedb',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      cmdclass={'optimize_upip': optimize_upip.OptimizeUpip},
      py_modules=['btreedb'])
