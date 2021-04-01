#!/usr/bin/env python3

import os
import sys
import time
import curses
import random
import pathlib
import sqlite3

# Early insert for custom packages
sys.path.insert(0, 'modules')

# Custom modules
#import maps
import utils
#import db_tool


# Defined functions
def refresh():
	# Simpler made screen refresh
	init.refresh()

def mkwin(line, col, x, y):
	# Example: mkwin(20, 7, 5, 40)
	# Convert cords to integers
	sx = int(line)
	sy = int(col)
	hight = int(x)
	width = int(y)
	curses.newwin(hight, width, sx, sy)

def addstr(x, y, msg):
	line = int(x)
	col = int(y)
	init.addstr(line, col, msg)



init = curses.initscr()