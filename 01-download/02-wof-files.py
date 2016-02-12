import glob
import fnmatch
import os
import pandas as pd 

drive = '/Users/danielmsheehan/'
wd = drive + 'GIS/projects/wofru/'
wk = wd + 'tasks/01-download/'
wi = wk + 'data/input/'
wp = wk + 'data/processing/'
wo = wk + 'data/output/'
wt = wk + 'data/tables/'

wofFiles = wi + 'wof/whosonfirst-data-master/data/'

matches = []
for root, dirnames, filenames in os.walk(wofFiles):
    for filename in fnmatch.filter(filenames, '*.geojson'):
        matches.append( (os.path.join(root, filename) ).replace(wofFiles,'').replace('.geojson','') )

df = pd.DataFrame(matches)

df.to_csv(wp+'wof_list.csv',index=False) #maybe first item from list could be removed, just 0