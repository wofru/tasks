import pandas as pd 
import os 
import urllib
import shutil

drive = '/Users/danielmsheehan/'
wd = drive + 'GIS/projects/wofru/'
wk = wd + 'tasks/01-download/'
wi = wk + 'data/input/'
wp = wk + 'data/processing/'
wo = wk + 'data/output/'
wt = wk + 'data/tables/'

inCSV = wp+'wof_list.csv'

df = pd.read_csv(inCSV)

df = df.fillna('')

df = df.head(25)

wd = '/Users/danielmsheehan/GIS/projects/wofru/tasks/05-website/JINJA2TEST/'
wd2 = '/Users/danielmsheehan/GitHub/wofru-tasks/05-website/testjinja/'
wofFiles = wi + 'wof/whosonfirst-data-master/data/'
webLoc = '/Users/danielmsheehan/GitHub/wofru.github.com/'

filenames = df['filename'].tolist()
wof_names = df['wof_name'].tolist()
boundboxs = df['boundbox'].tolist()


#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader

print '...making webpage dirs and copy existing geojson files'
for i in filenames:
  	newpath = webLoc+i
  	if not os.path.exists(newpath):
  		os.makedirs(newpath)
  	inFile = wofFiles+i+'.geojson'
  	z       = i.split('/')[:-1]
  	jsonloc = '/'.join(z)
  	#ouFile = newpath+'/'+jsonloc+'.geojson'
  	ouFile = webLoc+'/'+jsonloc + '/neighborhoods.geojson'
  	print i, inFile, ouFile
  	shutil.copy2(inFile, ouFile)	

for f, g, b in zip(filenames,wof_names,boundboxs):

	g = str(g.replace('/',''))
	#g = g.rsplit('/', 1)[1] #NEED TO FIGURE OUT THIS SPLIT, GO BACK TO IT
	#g = str(g)
	b = str(b) 
	wofName = g
	wofFile = f
	wofBoun = b
	PATH = os.path.dirname(os.path.abspath(__file__))
	TEMPLATE_ENVIRONMENT = Environment(
	    autoescape=False,
	    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
	    trim_blocks=False)


	def render_template(template_filename, context):
	    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


	def create_index_html():
	    fname = webLoc+f+".html"
	    urls = ['https://mapzen.com/', 'http://nygeog.com']
	    context = {
	        'urls': urls,
	        'wofName': wofName,
			'wofFile': wofFile,
			'wofBoun': wofBoun
	    }
	    #
	    with open(fname, 'w') as htmlFile:
	        # html = render_template('index.html', context)
	        # htmlFile.write(html)
	        # html = render_template('index_d3.html', context)
	        # htmlFile.write(html)
	        html = render_template('index_leaflet.html', context)
	        htmlFile.write(html)



	def main():
	    create_index_html()

	#############################################################################

	if __name__ == "__main__":
	    main()
