from setuptools import setup, find_packages

setup(name='IteratorDecorator',
      version='0.1',
      url='https://github.com/stovorov/IteratorDecorator',
      license='MIT',
      author='Pawel Stoworowicz',
      author_email='stoworow@gmail.com',
      description='Adds dynamically interface of iterator to class',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.rst').read(),
      zip_safe=False)
