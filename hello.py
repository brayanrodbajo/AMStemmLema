# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
#from flask import render_template
import os, sys
reload(sys)
sys.setdefaultencoding('utf8')
app = Flask(__name__)


@app.route('/')
def cargar():
	print 'Entro en cargar'
	return render_template('index.html')

@app.route('/', methods=['POST'])
def obtener(): 
	print "ENTRO en obtener"
	#os.system('analyze -f /usr/local/share/freeling/config/es.cfg tagged < /var/www/html/input.txt > /var/www/html/output.txt')
	#return 'hola mundo'
	texto=str(request.form['id_entrada'])
	print ("HOLA MUNDO!: ", texto)
	analisis_morfo =	ejecutarAnal(texto)
	print(analisis_morfo)
	return render_template('index.html', texto=texto, objetos=analisis_morfo)

def ejecutarAnal(cadena):
	# file=open("entrada.txt", "w")
	# file.write(cadena)
	# file.close()
	listaPalabras=[]
	listaLemas=[]
	listaStemm=[]
	listaEagles=[]
	#objeto={'pal':"", 'lema':"", 'stem':"", 'eagles':""}
	listaObjetos=[]


	limpio = cadena.replace('\r\n', ' ')
	palabras = limpio.split(' ')
	txt_analizado =""
	for pal in palabras:
		listaAM=str(os.popen('echo '+pal+'| analyze -f am.cfg').read()[:-1]).split()
		palabra=listaAM[0]
		#objeto['pal']=palabra
		txt_analizado += "PALABRA: "+palabra
		listaPalabras.append(palabra)
		
		lema=listaAM[1]
		#objeto['lema']=lema
		txt_analizado += "\n\t LEMA: "+lema
		listaLemas.append(lema)
		
		eagles=str(' '.join(listaAM[1:]))
		txt_analizado += "\n\t EAGLES: "+eagles
		listaEagles.append(eagles)
		#objeto['eagles']=eagles
		
		stemm = os.popen('php stemm_es.php "'+pal+'"').read()
		listaStemm.append(stemm)
		#objeto['stem']=stemm
		txt_analizado += "\n\t STEMM: "+stemm
		txt_analizado += '\n-----/-----\n'
		# txt_analizado += os.popen('echo '+pal+'| analyze -f am.cfg').read()[:-1]
		# txt_analizado += os.popen('php stemm_es.php "'+pal+'"').read()
		# txt_analizado += '\n'
		objeto=[palabra, lema, stemm, eagles]
		listaObjetos.append(objeto)

	#return [txt_analizado, listaPalabras, listaLemas, listaEagles, listaStemm]
	print listaObjetos
	return listaObjetos

# def leerArchivo():
# 	file=open("salida.txt", "r")
# 	morfo=""
# 	for line in file:		
# 		morfo+=line
# 	return morfo


if __name__ == '__main__': 
	app.run(host='0.0.0.0', debug=True, port=12345, use_reloader=True)
