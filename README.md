![My project-1](https://user-images.githubusercontent.com/126392767/221440135-35ee81c8-d322-4d13-9254-60a7fcc88da1.jpg)
![GitHub language count](https://img.shields.io/github/languages/count/firat-serge/voter-dashboard)
![GitHub language count](https://img.shields.io/github/languages/code-size/firat-serge/voter-dashboard?color=red)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firat-serge/voter-dashboard?color=orange)
# VOTERS DASHBOARD 
## Basic Overview
This is an academic project for an introduction into programming for a **_Masters in Geospatial technologies_** course 2023. This tool involved the creation of a database, ETL and API. The objective of this tool is to display voters related statistics. 
<br>The current state represents a work in progress of what is actually intended. Not all componnents are fully operational yet, but the schema below represents what the ultimate process ideally would look like.
![progprocess](https://user-images.githubusercontent.com/126392767/221442929-eed7d2f9-4f38-47fe-8169-ce533fcbf8c7.PNG)
The figure above represents the processess involved which included:
* Creating a database in a suitable format by downloading the data online and processing it using python 
* The coding process itself which was predominatly done using python and some R
* Extraction and visualization of the  data and given its geodata, the necessity of representation of some form of maps.
* The establishment of the dashboard itself which had to display information in various formats.
Various packages and extension are necessary to create the environment to enable us go from the database to the display of the dashboard. The packages necessary and database viewing are:
<br>`conda install --file requirements.txt --channel conda-forge`
<br>`View: sa.votes_geojson`
## Data
Data  for the dashboard is gotten online from where it is tranformed using the ETL Script. The data is transformed from shapefile to JSON.
## Database
The database is created in pgAdmin4. It is composed of a single table with multiple rows. Find attached the script for creating the database. <a href="https://github.com/firat-serge/voter-dashboard/commit/5441eb9404588791d2072bc3f53fe0b7bc48628c">creating table</a>
## ETL
Files are imported and processed. Some mathemathical functions are performed on some parts of the table creating further new columns whilst other data is removed from the table in a process of cleaning. <a href="https://github.com/firat-serge/voter-dashboard/blob/main/etl.py">etl</a>
## API
The API enables the user to get information from the database. 