#!/usr/bin/env python3

"""
Script that lets me compare my annual budget
with what I spend on a monthly basis.
"""

import os
from os.path import expanduser


def get_dir_path():
    """Get current users home directory path"""
    home = expanduser("~")
    return '{0}/budget_tracker/'.format(home)


def create_data_dir():
    """Create data dir if not exists"""
    # Data directory is created in current user's home dir
    directory = get_dir_path()
    if not os.path.exists(directory):
        os.mkdir(directory)


def update_data():
    """Update the csv file with new raw data"""
    directory = get_dir_path()
    with open('{0}data.csv'.format(directory), 'a') as data_file:
        data_file.write('New line\n')


if __name__ == '__main__':
    create_data_dir()
    update_data()
