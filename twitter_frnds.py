import urllib.request,urllib.parse, urllib.error
import json
import twurl
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


TWITTER_URL= 'https://api.twitter.com/1.1/friends/list.json'

while True:
    acc=input('Enter TwitterAcount')
    if(len(acc))<1:break
    url=twurl.augment(TWITTER_URL,{'screen_name': acc, 'count': '5'})
    print('Retreiving',url)
    connection=urllib.request.urlopen(url,context=ctx)
    data=connection.read().decode()
    js=json.loads(data)
    print(json.dumps(js,indent=2))

    headers=dict(connection.getheaders())
    print('Remaining count',headers['x-rate-limit-remaining'])

    for i in js['users']:
       print (i['screen_name'])
       s=i['status']['text']
       print(s)
    
