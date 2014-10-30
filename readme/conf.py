# -*- coding: utf-8 -*-

"""Configuration of the Readme app"""

from os.path import relpath, join, dirname

# Database
DB_NAME = relpath(join(dirname(__file__), 'data', 'readme.db'))
DB_TABLE = 'recommendation'

# JS Assets
JS_DIR = 'js'
JS_FILES = ['angular.js']
PACKED_JS = 'packed.js'

# CSS Assets
CSS_DIR = 'css'
CSS_FILES = ['base.css', 'bootstrap.css']
PACKED_CSS = 'packed.css'
