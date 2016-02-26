from urllib import urlopen
from jinja2 import Template

g = 1

html_str = urlopen('template.html').read() 

print html_str

Html_file= open('test.html',"w")
Html_file.write(html_str)
Html_file.close()