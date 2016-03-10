import os 
import pandas as pd
from jinja2 import Environment, FileSystemLoader

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

df['wof_url'] = 'http://wofru.github.io/' + df.filename.map(str) + '.html'

wd = '/Users/danielmsheehan/GIS/projects/wofru/tasks/05-website/JINJA2TEST/'
wd2 = '/Users/danielmsheehan/GitHub/wofru-tasks/05-website/testjinja/'
wofFiles = wi + 'wof/whosonfirst-data-master/data/'
webLoc = '/Users/danielmsheehan/GitHub/wofru.github.com/'

filenames = df['filename'].tolist()
wof_names = df['wof_name'].tolist()
boundboxs = df['boundbox'].tolist()
wof_urls  = df['wof_url'].tolist()

for i in wof_urls:
	print i

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
