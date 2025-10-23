#Using setup.py our ml project can be used as a package and can be deployed and implemented elsewehere

from setuptools import find_packages, setup
  
#contains metadata information about the project
setup(
    name='Fake News Detector',
    version='0.0.1',
    author='Sachin',
    author_email='bsachinmiryala@gmail.com',
    packages=find_packages()  #checks all files having constructor(init.py) and considers them as packages and builds them, once they are build we can use them to import
    # install_requires=get_requirements('requirements.txt')
) 