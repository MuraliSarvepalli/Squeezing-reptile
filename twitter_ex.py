import urllib.request, urllib.parse,urllib.error
import json
import twurl
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
TWITTER_URL='https://api.twitter.com/1.1/statuses/user_timeline.json'



while True:
    acct=input('Enter twitter account')
    if(len(acct)<1): break
    url=twurl.augment(TWITTER_URL,{'screen_name':acct,'count':'2'})
    print('Retrieving',url)
    connection=urllib.request.urlopen(url,context=ctx)
    data=connection.read().decode()
    print(data[:250])
    headers=dict(connection.getheaders())
    print ('REMAINING',headers['x-rate-limit-remaining'])

    
