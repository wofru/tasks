import pandas as pd 
import os 
import urllib
import shutil
from jinja2 import Environment, FileSystemLoader
from _settings import * 

#!/usr/bin/env python
print '...making webpage dirs and copy existing geojson files'
for i in filenames:
  	newpath = webLoc+i
  	if not os.path.exists(newpath):
  		os.makedirs(newpath)
  	inFile = wofFiles+i+'.geojson'
  	z       = i.split('/')[:-1]
  	jsonloc = '/'.join(z)
  	#ouFile = newpath+'/'+jsonloc+'.geojson'
  	ouFile = webLoc+'/'+jsonloc + '/wofru.geojson'
  	#print i, inFile, ouFile
  	shutil.copy2(inFile, ouFile)	
  	
	shutil.rmtree(webLoc+'/'+jsonloc+'/css')
	shutil.rmtree(webLoc+'/'+jsonloc+'/js')
	shutil.rmtree(webLoc+'/'+jsonloc+'/data')

	copyanything(d3css, webLoc+'/'+jsonloc+'/css')#+ '/css')
	copyanything(d3_js, webLoc+'/'+jsonloc+'/js')#+ '/js')
	copyanything(d3dat, webLoc+'/'+jsonloc+'/data')# + '/data')

for f, g, b in zip(filenames,wof_names,boundboxs):

	g = str(g.replace('/',''))
	#g = g.rsplit('/', 1)[1] #NEED TO FIGURE OUT THIS SPLIT, GO BACK TO IT
	#g = str(g)
	b = str(b) 
	wofName = g
	wofFile = f
	wofBoun = b
	NELat = b.split(',')[3]
	NELng = b.split(',')[2]
	SWLat = b.split(',')[1]
	SWLng = b.split(',')[0]

	PATH = os.path.dirname(os.path.abspath(__file__))
	TEMPLATE_ENVIRONMENT = Environment(
	    autoescape=False,
	    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
	    trim_blocks=False)

	def render_template(template_filename, context):
	    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

	def create_index_html():
	    fname = webLoc+f+".html"
	    urls = ['https://mapzen.com/', 'http://nygeog.com', 'http://wofru.github.io']
	    context = {
	        'urls': urls,
	        'wofName': wofName,
			'wofFile': wofFile,
			'wofBoun': wofBoun,
			'NELat': NELat,
			'NELng': NELng,
			'SWLat': SWLat,
			'SWLng': SWLng,
	    }
	    #
	    with open(fname, 'w') as htmlFile:
	        html = render_template('index.html', context)
	        htmlFile.write(html)
	    
	def main():
	    create_index_html()

	#############################################################################

	if __name__ == "__main__":
	    main()
