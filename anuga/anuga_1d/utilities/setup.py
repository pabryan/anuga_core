from __future__ import division, print_function

import os
import sys

from os.path import join

def configuration(parent_package='',top_path=None):
    
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    
    config = Configuration('utilities', parent_package, top_path)

    config.add_extension('util_ext',
                         sources=['util_ext.c'])
    
    return config
    
if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
