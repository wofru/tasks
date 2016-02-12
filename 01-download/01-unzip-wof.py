import zipfile

drive = '/Users/danielmsheehan/'
wd = drive + 'GIS/projects/wofru/'
wk = wd + 'tasks/01-download/'
wi = wk + 'data/input/'
wp = wk + 'data/processing/'
wo = wk + 'data/output/'
wt = wk + 'data/tables/'

inZip = wd + 'data/input/wof/whosonfirst-data-master.zip' #delete this input data
inZip = '/Users/danielmsheehan/Dropbox/whosonfirst-data-master.zip'

zfile = zipfile.ZipFile(inZip)
zfile.extractall(wi + 'wof/')