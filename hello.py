
from flask import Flask, render_template, request
import requests
app = Flask(__name__)#instancia

@app.route("/")#decoradores se asigna la ruta 
def hello_world():
    #return "<h1>Hello, World!</h1>"
    return render_template('home.html')

@app.route("/hola/<name>")#parametros se le agrega a la url
def hello(name):
    return render_template('hola.html', name=name)
@app.route('/rick/<page>')
def rickandmorty(page=1):
    
    url=f'https://rickandmortyapi.com/api/character/?page={page}'#le damos la pagina que queremos estar

    payload = ()
    headers= ()

    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.json())

    respuesta_json=response.json()#nos regresa un json
    info=respuesta_json['info']
    personajes=respuesta_json['results']#nos muestra  los resultados 
    
    next=int(page)+1#indicamos una pagina mas
    prev=int(page)-1#indicamos una paggina mes 
    return render_template('rick.html', personajes=personajes, next=next, prev=prev)#retornamos los parametros de personajes y las paginas mas y menos (previo  y siguiente)

@app.route('/search', methods=['GET', 'POST'])   #funcion para buscar
def search():
    search=request.form['search']
    if len(search)>0:
        url=f'https://rickandmortyapi.com/api/character/?name={search}'
        payload = ()
        headers= ()
        response = requests.request("GET", url, headers=headers, data=payload)
        #print(response.json())
        respuesta_json=response.json()#nos regresa un json
        info=respuesta_json['info']
        personajes=respuesta_json['results']
        if info['pages']>1:
            next=2
            prev=1
        else:
            next=1
            prev=1
        return render_template('rick.html', personajes=personajes, next=next, prev=prev)
    else:
        return 'No se pudo realizar la busqueda'

if __name__ == '__main__':
    app.run(debug=True)
    