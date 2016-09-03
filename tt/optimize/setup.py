#   setup.py
#   This script will build the main subpackages
#   See LICENSE for details


from numpy.distutils.misc_util import Configuration


def configuration(parent_package='', top_path=None):
    config = Configuration('optimize', parent_package, top_path)
    return config


if __name__ == '__main__':
    print('This is the wrong setup.py to run')
