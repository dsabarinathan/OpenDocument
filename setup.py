# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:42:38 2024

@author: SABARI
"""

from setuptools import setup , find_packages

setup(
      name = 'OpenDocument',
      version = '0.1',
      packages = find_packages(),
      install_requires =[
          # add depedencies here,
          # e.g. 'numpy>=1.11.1'
          'scikit-image==0.18.3',
          'numpy==1.20.0',
          'opencv-python==4.9.0.80'
          ],
      )
