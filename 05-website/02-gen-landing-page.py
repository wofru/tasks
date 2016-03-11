import os 
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from _settings import * 


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_index_html():
    fname = webLoc+"index.html"
    urls = ['https://mapzen.com/', 'http://nygeog.com']
    context = {
       'urls': wof_urls,
  #       'wofName': wofName,
		# 'wofFile': wofFile,
		# 'wofBoun': wofBoun,
		# 'NELat': NELat,
		# 'NELng': NELng,
		# 'SWLat': SWLat,
		# 'SWLng': SWLng,
    }
    #
    with open(fname, 'w') as htmlFile:
        html = render_template('index_landing.html', context)
        htmlFile.write(html)
    

def main():
    create_index_html()

#############################################################################

if __name__ == "__main__":
    main()
