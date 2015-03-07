import soundcloud

client = soundcloud.Client(access_token ='https://api.soundcloud/connect')
track  = client.get('./resolve',url='http://soundcloud.com/forss/flickermood')
print track.id


