#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name = Gospel PDF Viewer
Executable Command = gospel-pdf
Package Name = gospel-pdf
Python Module Name = gospel_pdf
Debian Dependency = python-qt4, python-poppler-qt4

Description = A poppler based PDF viewer written in PyQt4
Changes :
1.3.12  fixed : black page when opening a file with same name but lesser pages
1.3.13  window icon added

...........................................................................
|   Copyright (C) 2017-2018 Arindam Chaudhuri <ksharindam@gmail.com>       |
|                                                                          |
|   This program is free software: you can redistribute it and/or modify   |
|   it under the terms of the GNU General Public License as published by   |
|   the Free Software Foundation, either version 3 of the License, or      |
|   (at your option) any later version.                                    |
|                                                                          |
|   This program is distributed in the hope that it will be useful,        |
|   but WITHOUT ANY WARRANTY; without even the implied warranty of         |
|   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          |
|   GNU General Public License for more details.                           |
|                                                                          |
|   You should have received a copy of the GNU General Public License      |
|   along with this program.  If not, see <http://www.gnu.org/licenses/>.  |
...........................................................................
"""
# TODO: 
#       Show hyperlink target location at below like a browser
#       Rotate pages
#       Show fonts list
#       Show document info
#       Print File
#       Recent files list, clear recent option, clear history files
#       add highlight annotation
# FIXME : 
#       Search is not cancelled immediately, when cancel is pressed
#       

__version__ = '1.3.13'
