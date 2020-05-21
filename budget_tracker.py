#!/usr/bin/env python3

"""
Script that lets me compare my annual budget
with what I spend on a monthly basis.
"""

import os
from os.path import expanduser
import logging


def get_app_path():
    """Get current users home directory path"""
    home = expanduser("~")
    return '{0}/budget_tracker/'.format(home)


def logging_setup():
    """Set up log file directory path in current user's home dir"""
    log_dir = '{0}logs/'.format(get_app_path())
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
        logging.basicConfig(filename='{0}budget_tracker.log'.format(log_dir),
                            level=logging.DEBUG)
        logging.info('Created logging directory {0}'.format(log_dir))
    else:
        logging.basicConfig(filename='{0}budget_tracker.log'.format(log_dir),
                            level=logging.DEBUG)


def create_data_dir():
    """Create data dir if not exists"""
    # Data directory is created in current user's home dir
    directory = get_app_path()
    if not os.path.exists(directory):
        os.mkdir(directory)
        logging.info('Created app directory {0}'.format(directory))


def update_data():
    """Update the csv file with new raw data"""
    directory = get_app_path()
    with open('{0}data.csv'.format(directory), 'a') as data_file:
        data_file.write('New line\n')
        logging.info('Wrote new lines to {0}data.csv'.format(directory))


if __name__ == '__main__':
    logging_setup()
    create_data_dir()
    update_data()
