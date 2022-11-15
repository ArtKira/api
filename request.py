
import requests
url='https://rickandmortyapi.com/api/character'

payload = ()
headers= ()

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.json())

respuesta_json=response.json()
info=respuesta_json['info']
personaje=respuesta_json['results']


for item in personaje:
    print(item['name'], "Su estatus es ", item['status'])
    