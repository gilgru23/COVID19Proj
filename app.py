# movies.py

from flask import Flask, render_template,request
import requests
from flask_restful import Api,Resource


app = Flask(__name__)
api=Api(app)
lastdays={'lastdays':31};#For calculating diffrences between days I need the day before the 30th day
def deathsPeak(country):
  return calculatePeak(country,'deaths','deathsPeak')

def recoveredPeak(country):
  return calculatePeak(country,'recovered','recoveredPeak')

def newCasesPeak(country):
  return calculatePeak(country,'cases','newCasesPeak')

def calculatePeak(country,term,methodName):
  global status
  r = requests.get('https://disease.sh/v3/covid-19/historical/' + country, params=lastdays)
  if r.status_code == 404:#checks if the country name is valid for out api request
    status=-1 #the contact with the api was failed
    return {}
  status = 1  #the contact with the api was succeded
  parsed = r.json()#parse the json into a dictionary
  filtered = dict(parsed['timeline'][term])
  currPeakValue = 0
  dateOfCurrPeak = ''
  lastDate = ''
  count = 0
  for date in filtered.keys():
    if (count == 0):  # I don't calculate the first item- the 31st day
      count += 1
      lastDate = date
      continue
    else:
      dailyValue=filtered[date] - filtered[lastDate]
      if(term=='cases'):
        currrNumOfDeaths=parsed['timeline']['deaths'][date]-parsed['timeline']['deaths'][lastDate]
        currNumOfRecovered=parsed['timeline']['recovered'][date]-parsed['timeline']['recovered'][lastDate]
        dailyValue = dailyValue- currrNumOfDeaths-currNumOfRecovered #for each day the number of the new cases=total num of cases the today-total num of cases yesterday-numberOfDeathsToday-numberOfRecoveredToday
      if (dailyValue > currPeakValue):
        currPeakValue = dailyValue
        dateOfCurrPeak = date
      lastDate = date
  return {"country":country,"method":methodName,"date":dateOfCurrPeak,"value":currPeakValue}

class Router(Resource):
  def get(self,method):
    countryName=request.args.get('country')#get the query after country?
    if(countryName):#checks if arguement country argument was entered
      if(method=='newCasesPeak'):
        return newCasesPeak(countryName)
      if (method == 'recoveredPeak'):
        return recoveredPeak(countryName)
      if (method == 'deathsPeak'):
        return deathsPeak(countryName)
    else:
      if(method=='status'):
        if(status==1):
          return {"status":"success"}
        if(status==-1):
          return {"status":"fail"}
        #Todo:check what to do if there wasn't a call to the api yet
    return {}

api.add_resource(Router,'/<string:method>')

if __name__ == '__main__':
  app.run(debug=True)
