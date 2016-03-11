import pandas as pd
import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

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

df = df.head(50)

df['wof_url'] = 'http://wofru.github.io/' + df.filename.map(str) + '.html'

wd = '/Users/danielmsheehan/GIS/projects/wofru/tasks/05-website/JINJA2TEST/'
wd2 = '/Users/danielmsheehan/GitHub/wofru-tasks/05-website/testjinja/'
wofFiles = wi + 'wof/whosonfirst-data-master/data/'
webLoc = '/Users/danielmsheehan/GitHub/wofru.github.com/'

filenames = df['filename'].tolist()
wof_names = df['wof_name'].tolist()
boundboxs = df['boundbox'].tolist()
wof_urls  = df['wof_url'].tolist()

d3_js = '/Users/danielmsheehan/GitHub/wofru-tasks/05-website/templates/d3/time-series-plot/js'
d3css = '/Users/danielmsheehan/GitHub/wofru-tasks/05-website/templates/d3/time-series-plot/css'
d3dat = '/Users/danielmsheehan/GitHub/wofru-tasks/05-website/templates/d3/time-series-plot/data'
