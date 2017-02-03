## SHALLOW WATER MODEL
"""
Copyright (C) 2017,  Milan Kloewer (mkloewer@geomar.de)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Hopefully, there will be soon a documentation available.
"""

from __future__ import print_function
path = '/home/mkloewer/python/swm/'

# import modules
import os; os.chdir(path)
import numpy as np
from scipy import sparse
import time as tictoc
from netCDF4 import Dataset
import glob
import zipfile

## import all functions
exec(open(path+'swm_param.py').read())
exec(open(path+'swm_operators.py').read())
exec(open(path+'swm_rhs.py').read())
exec(open(path+'swm_integration.py').read())
exec(open(path+'swm_output.py').read())

## set all parameters and initial conditions, and run model
u,v,h = set_param()
u,v,h = time_integration(u,v,h)
