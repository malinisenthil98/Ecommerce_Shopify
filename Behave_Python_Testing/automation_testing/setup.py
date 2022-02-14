# from distutils.core import setup
from setuptools import setup
setup(name='Behave_Python_Testing',
      version='1.0',
      description='Automation Testing',
      author='Malini Senthilkumar',
      author_email='malinisenthil.acumen@gmail.com',
      packages=[
            'BDDCommon',
            'BDDCommon.CommonFuncs',
            'BDDCommon.CommonSteps',
            'BDDCommon.CommonConfigs'
      ],
     )

