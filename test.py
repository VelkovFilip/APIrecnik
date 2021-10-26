import requests

BASE = 'https://hoyoapi.herokuapp.com'
data = {}
data['ip_address'] = '89.206.255.126'
response = requests.get(BASE +"/device/1" )
#response = requests.get(BASE +"/restaurants" )
#response = requests.get(BASE + '/restaurant/5')
print(response.json())
