import Data.Headers as header
import Data.urls as url
import requests as web
import json

teamID = input("Team ID: ")
print(web.get(url.RallycryAccountContacts.format(teamID), headers=header.RallycryHeaders).text)
