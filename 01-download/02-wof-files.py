import glob
import fnmatch
import os
import pandas as pd 
import json

drive = '/Users/danielmsheehan/'
wd = drive + 'GIS/projects/wofru/'
wk = wd + 'tasks/01-download/'
wi = wk + 'data/input/'
wp = wk + 'data/processing/'
wo = wk + 'data/output/'
wt = wk + 'data/tables/'

#wofFiles = wi + 'wof/whosonfirst-data-master/data/1/' #TEST
wofFiles = wi + 'wof/whosonfirst-data-master/data/'

matches = []
gnames  = []

for root, dirnames, filenames in os.walk(wofFiles):
    for filename in fnmatch.filter(filenames, '*.geojson'):
        matches.append( (os.path.join(root, filename) ).replace(wofFiles,'').replace('.geojson','') )
      	with open(root + '/' + filename) as data_file:     		
    		try:
    			data = json.load(data_file)
	    		name = data["properties"]["wof:name"]
	    		gnames.append(name)
	    	except:
	    		#print data_file
	    		gnames.append('quatroshapes or naturalearth')

df = pd.DataFrame(({'filename' : matches, 
 'wof_name': gnames
  }))

df.to_csv(wp+'wof_list.csv',index=False,encoding='utf-8') #maybe first item from list could be removed, just 0