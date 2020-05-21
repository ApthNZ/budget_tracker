#!usr/bin/env python3

"""
Test file for checking necessary directories and files are present.
"""

import os
from os.path import expanduser
import logging


class TestStructure:
    """Test the structure is in place before we read and write data"""

    def test_dir(self):
        """Make sure the data directory exists"""
        home = expanduser("~")
        assert os.path.exists('{0}/budget_tracker/'.format(home))

    def test_file(self):
        """Make sure the data csv exists"""
        home = expanduser("~")
        assert os.path.exists('{0}/budget_tracker/data.csv'.format(home))
