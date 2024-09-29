import Data.Headers as header
import Data.urls as url
import requests as web
import json

#Vars
CompID = input("Competition Id: ")
teamsFile = open("Utils\\Data\\teams.json", "w", encoding="utf-8")

#Web Requests
response = web.get(url.CompetitionPage.format(CompID, 1))
responseJson = json.loads(response.text)
compName = json.loads(web.get(url.CompetitionPage.format(CompID, 1)).text)["content"][0]["competition"]["name"]

TeamsInComp = responseJson["totalElements"]
newResponse = web.get(url.CompetitionPage.format(CompID, TeamsInComp))

if newResponse.status_code != 200:
    print("Error: {}".format(newResponse.status_code))
else:
    teamsFile.write(newResponse.text)
    print("Complete, Loaded {} Teams".format(TeamsInComp))

compNameFile = open("Utils\\Data\\compname.py", "w")
compNameFile.write("CompName = \'{}\'".format(compName))
compNameFile.close()
teamsFile.close()