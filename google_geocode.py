import urllib.request, urllib.parse,urllib.error
import json

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    add=input('Enter Location')
    if len(add)<1:
        break
    url=serviceurl+urllib.parse.urlencode({'address':add})
    print (url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print (data)

    js=json.loads(data)
    print (js)
    print (json.dumps(js,indent=4))
    lat=js["results"][0]["geometry"]["bounds"]["northeast"]
    addr=js["results"][0]["formatted_address"]
    shortname=js["results"][0]["address_components"][2]["short_name"]
    print (lat)
    print (addr)
    print (shortname)
