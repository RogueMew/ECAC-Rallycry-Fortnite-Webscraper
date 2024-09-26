import requests as web
import Headers as header
import urls as url
import json

user = input("Username: ")
RequestURL = "https://fortnite-api.com/v2/stats/br/v2"
print(web.get(RequestURL, headers=header.Fortnite_ApiHeader, params={'name': user}).text)