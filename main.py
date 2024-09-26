import requests as web
import json
import Headers as header
import urls as url
def newLine():
    print("\n")       

accountInfo = "https://fortnite-api.com/v2/stats/br/v2"
tracker = "https://fortnitetracker.com/profile/all/{}"

file = open('teams.json', 'r')
data = json.load( open("teams.json", "r"))["content"]
teams = []
for team in data:
    teams.append(team["id"])
for team in teams:
    newLine()
    response = web.get(url.RallycryAccountContacts.format(team), headers=header.RallycryHeaders)

    if response.status_code != 200:
        if response.status_code == 400:
            print("Code: {}, Bad Request".format(response.status_code))
        
        elif response.status_code == 401:
            print("Code: {}, Unauthorized".format(response.status_code))
        
        elif response.status_code == 403:
            print("Code: {}, Forbidden".format(response.status_code))
        exit()
    elif response.status_code == 200:
        response_json = json.loads(response.text)["content"]
    
    print("{}: ".format(json.loads(web.get(url.TeamPage.format(team)).text)["alternateName"]))
    listLength = len(response_json)
    x = 0
    while x < listLength:
        if response_json[x]["network"] == "EPIC":
            newLine()
            print("    Epic Games: {}".format(response_json[x]["handle"]))
            accountInfoResponse = web.get(accountInfo, headers=header.Fortnite_ApiHeader,params={'name':response_json[x]["handle"]})
            if list(json.loads(accountInfoResponse.text).keys())[1] == "error":
                print("    Account Doesnt Exist")
            else:
                print("    Level:{}".format(json.loads(accountInfoResponse.text)["data"]["battlePass"]["level"]))
                tempDictionary = {
                    'KBM':0,
                    'Console':0,
                    'Mobile':0
                }
                if "keyboardMouse" in list(json.loads(accountInfoResponse.text)["data"]["stats"].keys()):
                    tempDictionary["KBM"] = json.loads(accountInfoResponse.text)["data"]["stats"]["keyboardMouse"]["overall"]["minutesPlayed"]
                if "gamepad" in list(json.loads(accountInfoResponse.text)["data"]["stats"].keys()):
                    tempDictionary["Console"] = json.loads(accountInfoResponse.text)["data"]["stats"]["gamepad"]["overall"]["minutesPlayed"]
                if "touch" in list(json.loads(accountInfoResponse.text)["data"]["stats"].keys()):
                    tempDictionary["Mobile"] = json.loads(accountInfoResponse.text)["data"]["stats"]["touch"]["overall"]["minutesPlayed"]
                
                print("    Most Played Platform: {}".format(max(tempDictionary, key=tempDictionary.get)))
                print("    Time played on platform:")
                print("        Console: {} minutes".format(tempDictionary["Console"]))
                print("        Mobile: {} minutes".format(tempDictionary["Mobile"]))
                print("        Keyboard and Mouse: {} minutes".format(tempDictionary["KBM"]))

                    
            x = x +1
        elif response_json[x]["network"] == "DISCORD" and response_json[x-1]["user"]["id"] != response_json[x]["user"]["id"]:
            newLine()
            print("    Discord: {}".format(response_json[x]["handle"]))
            x = x + 1
        elif response_json[x]["network"] == "DISCORD" and response_json[x-1]["user"]["id"] == response_json[x]["user"]["id"]:
            print("    Discord: {}".format(response_json[x]["handle"]))
            x =x + 1