## Description
* Something that “rolls up” stats by Who’s On First neighbourhoods, city, county, state, country, and globally about data in OSM or other sources. 
* That presents that in a generated website with "pages" for each of those features and their individual roll up, with an eye towards trends and projections. 
* Updates itself on some cadence, say weekly, so the data doesn’t go stale. Something that leverages AWS infrastructure to do some of the heavy lifting. 

## To Do
* Create instance and AMI (maybe Windows to start) for donwloading the data. Could test on Parallels version. 
* 44 GB's for OSM global (double check this). 
* How large is Who's on First? 

## Workflow
* Spin up ec2 instances, weekly, monthly, etc. 
* Run download scripts
  * OSM
  * Who's on First
* Push data into PostgreSQL (PostGIS enabled) via psycopg2
* Run geoprocessing scripts OSM against Who's on First gazateer (intersect)
* Do some basic descriptive statistics (in Pandas or with Python-SQL wrapper)
* Push stats out to files (csv or json)
* Script to generate website (html, js, etc.)
* Site hosted on github.io site, using d3, generate graphics and charts

## AWS Notes
* How can I script up spinning up ec2 instances?
  * [AWS Python SDK](https://aws.amazon.com/developers/getting-started/python/)    
* Can I force them to run the download and CREATE TABLE OR INTERSECT scripts? 
* Should I leave my RDS instances up and running or should I export them and save them on S3?
  * Fuck no, shut them down when done with analysis. 
* RDS snapshots will be stored on s3, but access them RDS console.

## What do I want to show???

1. Maybe one of the lines in the graph can be population growth from 2000, 2010 and the most recent ACS???? using area-weighted interpolation

2. Maybe another or all of the lines can be OSM edits/commits or something by type
