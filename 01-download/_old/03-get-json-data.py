import json
import pandas as pd

inJSN = '/Users/danielmsheehan/GIS/projects/wofru/tasks/01-download/data/input/wof/whosonfirst-data-master/data/1/1.geojson'
/Users/danielmsheehan/GIS/projects/wofru/tasks/01-download/data/input/wof/whosonfirst-data-master/data/1/1.geojson'
/Users/danielmsheehan/GIS/projects/wofru/tasks/01-download/data/input/wof/whosonfirst-data-master/data/00.geojson'
# d = pd.read_json(inJSN)

# print d['properties']



# data = json.loads(inJSN)

# #print data
# json_normalize(data['properties'])


#http://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime

import json
from pprint import pprint

with open(inJSN) as data_file:    
    data = json.load(data_file)
pprint(data)

name = data["properties"]["wof:name"]

print name