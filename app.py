
from flask import Flask, render_template,request
import requests
from flask_restful import Api,Resource
from multiprocessing import Process

app = Flask(__name__)
api=Api(app)

#Global varaibles
lastdays={'lastdays':31};#For calculating diffrences between days I need the day before the 30th day
status=-1

#endpoint function
def deathsPeak(country):
  return calculatePeak(country,'deaths','deathsPeak')

def recoveredPeak(country):
  return calculatePeak(country,'recovered','recoveredPeak')

def newCasesPeak(country):
  return calculatePeak(country,'cases','newCasesPeak')

# The function that centralizes the logic behind the endponits- code reusable
def calculatePeak(country,term,methodName):
  global status
  r = requests.get('https://disease.sh/v3/covid-19/historical/' + country, params=lastdays)
  if r.status_code == 404:#checks if the country name is valid for out api request
    status=-1 #the contact with the api was failed
    return {}
  status = 1  #the contact with the api was succeded
  parsed = r.json() #parse the json into a dictionary type
  filtered = dict(parsed['timeline'][term])
  currPeakValue = 0
  dateOfCurrPeak = ''
  global lastDate
  count = 0
  for date in filtered.keys(): #iterating all the dates
    if (count == 0):  # I don't calculate the first item- the 31st day
      count += 1
      lastDate = date
      continue
    else:
      dailyValue=filtered[date] - filtered[lastDate]
      if(term=='cases'):
        currrNumOfDeaths=parsed['timeline']['deaths'][date]-parsed['timeline']['deaths'][lastDate]
        currNumOfRecovered=parsed['timeline']['recovered'][date]-parsed['timeline']['recovered'][lastDate]
        dailyValue = dailyValue- currrNumOfDeaths-currNumOfRecovered #for each day the number of today's new cases=total num of cases today-(total num of cases yesterday-numberOfDeathsToday-numberOfRecoveredToday)
      if (dailyValue > currPeakValue):#finds the maximum
        currPeakValue = dailyValue
        dateOfCurrPeak = date
      lastDate = date
  return {"country": country, "method": methodName, "date": dateOfCurrPeak, "value": currPeakValue}

#additional methods
def shutdown_server():#responsible for the graceful shutdown when requeted
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  func()

class Router(Resource):#responsible to navigate the requets to the right operation
  def get(self,method):
    method=str(method).replace(" ", "")#prevent spaces to collapse the sever
    countryName=str(request.args.get('country')).replace(" ", "")#get the query after country?, prevent spaces to collapse the sever
    if(countryName):#checks if arguement country argument was entered
      if(method=='newCasesPeak'):
        return newCasesPeak(countryName)
      if (method == 'recoveredPeak'):
        return recoveredPeak(countryName)
      if (method == 'deathsPeak'):
        return deathsPeak(countryName)
    else:
      if (method == 'shutdown'):
        shutdown_server()
        return {"status":"terminated"}
      if(method=='status'):
        if(status==1):
          return {"status":"success"}
        if(status==-1):
          return {"status":"fail"}
    return {}

api.add_resource(Router,'/<string:method>')#activate the Router above




if __name__ == '__main__':
  app.run(debug=True)
