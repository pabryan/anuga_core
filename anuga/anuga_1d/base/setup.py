from __future__ import division, print_function

import os
import sys

from os.path import join

def configuration(parent_package='',top_path=None):
    
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    
    config = Configuration('base', parent_package, top_path)

    util_dir = join('..','utilities')
            
    config.add_extension('quantity_ext',
                         sources=['quantity_ext.c'],
                         include_dirs=[util_dir])
    
    return config
    
if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
