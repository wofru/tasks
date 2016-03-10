import pandas as pd 
import os 
import urllib

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

wd = '/Users/danielmsheehan/GIS/projects/wofru/tasks/05-website/'

filenames = df['filename'].tolist()
wof_names = df['wof_name'].tolist()
boundboxs = df['boundbox'].tolist()

print '...making webpage dirs'
# for i in filenames:
#   newpath = wd+i
#   if not os.path.exists(newpath):
#     os.makedirs(newpath)

print '...making html files'
for f, g, b in zip(filenames,wof_names,boundboxs):
  try:
    g = str(g)
    #g = g.rsplit('/', 1)[1] #NEED TO FIGURE OUT THIS SPLIT, GO BACK TO IT
    #g = str(g)
    b = str(b)  
    html_str = urlopen('template.html').read()    
    # '''
    # '''
  except:
    #print f, g, b
    html_str = '<p>something went wrong</p>'

    

#for theVar, varTheme,varName,vizID in zip(theVars,varThemes,varNames,vizIDs):
#for theVar, varTheme,varName,vizID in zip(theVars,varThemes,varNames,vizIDs):
    # csvUrl = varTheme.replace('-','_') + '.csv&format=csv&q=SELECT geoid,' + ','.join(theVar) +  ' FROM ct10'
    # shpUrl = varTheme.replace('-','_') + '&format=shp&q=SELECT the_geom,geoid,' + ','.join(theVar) +  ' FROM ct10'
    
    #dictUrl = '../../../data/dictionary/'+varTheme+'.html'
    
    
    # html_str = '''<html>
    # <head>
    #   <meta name="viewport" content="width=device-width, initial-scale=1">
    #   <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    #   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    #   <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    #   <link rel="stylesheet" href="http://libs.cartocdn.com/cartodb.js/v3/3.11/themes/css/cartodb.css" />
    #   <script src="http://libs.cartocdn.com/cartodb.js/v3/3.11/cartodb.js"></script>
    #   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    #   <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    #   <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    #   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    #   <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    
    #   <link rel="stylesheet" href="css/style.css">   <!-- LOCAL FILE -->
    #   <!-- <script src="js/'''+varTheme+'''_script.js"></script>    LOCAL FILE -->
    # </head>
    
    # <body onload="init()">
    #   <div id='map'></div>
    #   <!-- LEFT PANEL IS SAME FOR EVERY PAGE -->
    #   <div id="leftpanel">

    #     <button class="btn btn-default dropdown-toggle" type="button" id="menu1"><a href="../../../" class="button all">Home</a>
    #         </button>
    #     <button class="btn btn-default dropdown-toggle" type="button" id="menu1"><a href="../../../data/download.html" class="button all">All Data</a>
    #         </button>
    #     <button class="btn btn-default dropdown-toggle" type="button" id="menu1"><a href="" class="button all">Reset</a>
    #         </button>
    
    #       <div class="dropdown">
    #         <button class="btn btn-default dropdown-toggle" type="button" id="menu1" data-toggle="dropdown">Variables
    #         <span class="caret"></span></button>
    #         <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">
    #           '''+dropdownHTML+'''
    #         </ul>
    #       </div>
    #     </div>
    #   </div>
    #   <!-- LEFT PANEL IS SAME FOR EVERY PAGE -->
    #   <div id='exports'>
          
    #       <button onclick='location.href="'''+dictUrl+'''"'>'''+varName+''' <strong>Data dictionary</strong></button>
    #       <p></p>
    #       <button onclick='location.href="'''+api_pre+csvUrl+'''"'><strong>Export</strong> '''+varName+''' data as <strong>CSV</strong></button>
    #       <p></p>
    #       <button onclick='location.href="'''+api_pre+shpUrl+'''"'><strong>Export</strong> '''+varName+''' data as <strong>Shapefile</strong></button>
    #    </div>
    #    <!-- ALL DATA PANEL IS OFF - SEE LEFTPANEL
    #    <div id='alldata'>
    #       <p></p>
    #       <button onclick='location.href="../../../data/download.html"'>Download master data</button>
    #    </div> -->
    # </body>
    # </html>'''
    
    
  Html_file= open(wd+f+'.html',"w")
  Html_file.write(html_str)
  Html_file.close()