import requests as web
import Utils.Data
import Utils.Data.Headers as header
import Utils.Data.compname
import Utils.Data.urls as url
import Utils.Data.compname as var
import json

def newLine():
    print("")  

def writeNewLine():
    savefile.write("\n")

accountInfo = "https://fortnite-api.com/v2/stats/br/v2"
tracker = "https://fortnitetracker.com/profile/all/{}"
print("Loading Data from: {}".format(var.CompName) )
newLine()
savefile = open('./Output/{}.txt'.format(input("Ouput File Name: ")), "w",encoding="utf-8")
data = json.load( open("./Utils/Data/teams.json", "r"))["content"]
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
        if json.loads(response.text)== {}:
            
            tempText = "{}: ".format(json.loads(web.get(url.TeamPage.format(team), header.RallycryHeaders).text)["alternateName"])
            print(tempText)
            
            writeNewLine()
            savefile.write(tempText)
            writeNewLine()
            
            communityId = json.loads(web.get(url.TeamPage.format(team), header.RallycryHeaders).text)["representing"]["id"]
            
            if web.get(url.CommunityPage.format(communityId),header.RallycryHeaders).status_code == 200:
                tempText = "    Representing: {}".format(json.loads(web.get(url.CommunityPage.format(communityId)).text)["content"][0]["community"]["name"])
                print(tempText)
                
                savefile.write(tempText)
                writeNewLine()
            
            tempText = "    Empty team"
            newLine()
            print(tempText)
            
            writeNewLine()
            savefile.write(tempText)
            writeNewLine()

        else:
            response_json = json.loads(response.text)["content"]
            tempText = "{}: ".format(json.loads(web.get(url.TeamPage.format(team), header.RallycryHeaders).text)["alternateName"])
            writeNewLine()
            print(tempText)
            savefile.write(tempText)
            writeNewLine()

            communityId = json.loads(web.get(url.TeamPage.format(team), header.RallycryHeaders).text)["representing"]["id"]
            if web.get(url.CommunityPage.format(communityId),header.RallycryHeaders).status_code == 200:
                tempText = "    Representing: {}".format(json.loads(web.get(url.CommunityPage.format(communityId)).text)["content"][0]["community"]["name"])
                print(tempText)
                savefile.write(tempText)
                writeNewLine()
            
            listLength = len(response_json)
            x = 0
            while x < listLength:
                if response_json[x]["network"] == "EPIC" and response_json[x-1]["user"]["id"] != response_json[x]["user"]["id"]:
                    tempText = "    Epic Games: {}".format(response_json[x]["handle"])
                    newLine()
                    writeNewLine()
                    
                    savefile.write(tempText)
                    print(tempText)
                    
                    writeNewLine()

                    accountInfoResponse = web.get(accountInfo, headers=header.Fortnite_ApiHeader,params={'name':response_json[x]["handle"]})
                    
                    if response_json[x]["handle"] == "N/A":
                        tempText = "    Not Applicable"
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()

                    elif list(json.loads(accountInfoResponse.text).keys())[1] == "error":
                        if json.loads(accountInfoResponse.text)["error"] == "the requested account's stats are not public":
                            tempText = "    Stats are Private"
                            print(tempText)
                            savefile.write(tempText)
                            writeNewLine()
                        else:
                            tempText = "    Account Doesnt Exist"
                            print(tempText)
                            savefile.write(tempText)
                            writeNewLine()
                    else:
                        tempText = "    Level:{}".format(json.loads(accountInfoResponse.text)["data"]["battlePass"]["level"])
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()

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
                        
                        tempText = "    Most Played Platform: {}".format(max(tempDictionary, key=tempDictionary.get))
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()

                        tempText = "    Time played on platform:" 
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()
                        
                        tempText = "        Console: {} minutes".format(tempDictionary["Console"])
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()
                        
                        tempText = "        Mobile: {} minutes".format(tempDictionary["Mobile"]) 
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()
                        
                        tempText = "        Keyboard and Mouse: {} minutes".format(tempDictionary["KBM"]) 
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()

                            
                    x = x +1
                elif response_json[x]["network"] == "EPIC" and response_json[x-1]["user"]["id"] == response_json[x]["user"]["id"]:
                    tempText = "    Epic Games: {}".format(response_json[x]["handle"])
                    
                    savefile.write(tempText)
                    print(tempText)
                    
                    writeNewLine()

                    accountInfoResponse = web.get(accountInfo, headers=header.Fortnite_ApiHeader,params={'name':response_json[x]["handle"]})
                    
                    if list(json.loads(accountInfoResponse.text).keys())[1] == "error":
                        tempText = "    Account Doesnt Exist"
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()
                    else:
                        tempText = "    Level:{}".format(json.loads(accountInfoResponse.text)["data"]["battlePass"]["level"])
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()

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
                        
                        tempText = "    Most Played Platform: {}".format(max(tempDictionary, key=tempDictionary.get))
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()

                        tempText = "    Time played on platform:" 
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()
                        
                        tempText = "        Console: {} minutes".format(tempDictionary["Console"])
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()
                        
                        tempText = "        Mobile: {} minutes".format(tempDictionary["Mobile"]) 
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()
                        
                        tempText = "        Keyboard and Mouse: {} minutes".format(tempDictionary["KBM"]) 
                        print(tempText)
                        savefile.write(tempText)
                        writeNewLine()

                            
                    x = x +1
                elif response_json[x]["network"] == "DISCORD" and response_json[x-1]["user"]["id"] != response_json[x]["user"]["id"]:
                    newLine()
                    writeNewLine()
                    
                    tempText = "    Discord: {}".format(response_json[x]["handle"]) 
                    print(tempText)
                    savefile.write(tempText)

                    x = x + 1
                elif response_json[x]["network"] == "DISCORD" and response_json[x-1]["user"]["id"] == response_json[x]["user"]["id"]:
                    tempText = "    Discord: {}".format(response_json[x]["handle"]) 
                    
                    print(tempText)
                    savefile.write(tempText)
                    writeNewLine()

                    x =x + 1
        

savefile.close()
print("Completed")