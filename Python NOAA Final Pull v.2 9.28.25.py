import requests
import json

#set the token needed for the NOAA API
#uncomment and replace the text with your own token

#token = 'private token goes here for NOAA API'

#convert token to dict object for use in http header
# uncomment the next line once token is set
creds = dict(token=token)

#set the url for the request for 4 different zip codes in NC for summer 2019

UrlList = ['https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:27601&datatypeid=PRCP&datatypeid=TMIN&datatypeid=TMAX&startdate=2019-06-01&enddate=2019-08-31&units=standard&limit=1000', 
           'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&datatypeid=PRCP&datatypeid=TMIN&datatypeid=TMAX&startdate=2019-06-01&enddate=2019-08-31&units=standard&limit=1000',
           'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:27260&datatypeid=PRCP&datatypeid=TMIN&datatypeid=TMAX&startdate=2019-06-01&enddate=2019-08-31&units=standard&limit=1000',
           'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28516&datatypeid=PRCP&datatypeid=TMIN&datatypeid=TMAX&startdate=2019-06-01&enddate=2019-08-31&units=standard&limit=1000']


#url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/locationcategories'
 #^ gives location categories "ST" "ZIP" :CNTY" county, "CITY".

#parameters for the request and project instructions
#id value Daily summaries "GHCND" looking for id "PRCP" for Precipitation (name "Preceipitation"), id "TEMP" for temperature, #min date and max daate of 2019-06-16

#use the requests' get function to make the http request and assign the result to a variable

#define a variable that will hold all json data
json_data = None

#open a .json file in write mode on PC path
f = open(r"C:\DIGA\NOAA.json","w")
for url in UrlList:
    r = requests.get(url, headers=creds)
    if json_data is None:
        #if json_data is None, assign the first response to json_data
        json_data = r.json()
    else:
        json_data['results'].extend(r.json()['results'])


#print the result message
r_pretty= json.dumps(json_data, indent=2)
print(r_pretty)

#print the text (body) portion of the response
print(r_pretty)

#write the response data to the json file
f.write(r_pretty)

#close the file
f.close()

#load the json into a python dict
output = json.loads(r.text)


#notes
##print out the first result
##print(output['results'][0])
#geojson https://gist.github.com/Spaxe/94e130c73a1b835d3c30ea672ec7e5fe

# open a .json file in write mode
# f = open(r"C:\DIGA\NOAA.json","w")