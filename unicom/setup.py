from distutils.core import setup
import py2exe

setup(
	options={'py2exe':{'excludes':['readline']}},
	console=['convert.py']
	)

#    setup(
#    options={'py2exe':{'excludes':['Image','PIL._imagingagg','PyQt4',
#    'PyQt5','_abcoll','_imaging_gif','_util','cffi','lxml','openpyxl.tests',
#    'readline','tkinter']}},
#     )