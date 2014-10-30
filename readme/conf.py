# -*- coding: utf-8 -*-

"""Configuration of the Readme app"""

from os.path import relpath, join, dirname

DB_NAME = relpath(join(dirname(__file__), 'data', 'readme.db'))
DB_TABLE = 'recommendation'
