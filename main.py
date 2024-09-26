import requests as web
import json
import Headers as header
import urls as url
def newLine():
    print("\n")       

accountID = "https://fortniteapi.io/v1/lookup?username={}"
Account_Level = "https://fortniteapi.io/v1/stats?account={}"
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
            
            account = json.loads(web.get(accountID.format(response_json[x]["handle"]), headers=header.FortniteApiIOHeaders).text)
            if list(account.keys())[1] == "error" and account["error"]["code"] != 'INVALID_API_KEY':
                print("    Username Incorrect or Not Findable")
                print("    check link bellow")
            elif list(account.keys())[1] == "error" and account["error"]["code"] == 'INVALID_API_KEY':
                print("    Invalid API Key")
                exit()
            else:
                if json.loads(web.get(Account_Level.format(account["account_id"]),headers=header.FortniteApiIOHeaders).text)["result"] == False:
                    print("    Account Private")
                else:
                    print("    level: {}".format(json.loads(web.get(Account_Level.format(account["account_id"]), headers=header.FortniteApiIOHeaders).text)["account"]["level"]))
            print("    {}".format(tracker.format(response_json[x]["handle"])))        
            x = x +1
        elif response_json[x]["network"] == "DISCORD" and response_json[x-1]["user"]["id"] != response_json[x]["user"]["id"]:
            newLine()
            print("    Discord: {}".format(response_json[x]["handle"]))
            x = x + 1
        elif response_json[x]["network"] == "DISCORD" and response_json[x-1]["user"]["id"] == response_json[x]["user"]["id"]:
            print("    Discord: {}".format(response_json[x]["handle"]))
            x =x + 1