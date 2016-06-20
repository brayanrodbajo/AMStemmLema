# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import os, sys
from generador import *
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
	texto=str(request.form['id_entrada'])
	print ("Texto Recibido: ", texto)
	trees=["a","b"]
	# trees=crear_arboles(texto)
	#print(analisis_morfo)
	return render_template('index.html', texto=texto, tr_stanford=trees[0], tr_bikel=trees[1], result_precision_bikel="0.1", result_recall_bikel="0.11", result_precision_stanford="0.8", result_recall_stanford="0.88")

def crear_arboles(cadena):
	listaObjetos=[]
	limpio = cadena.replace('\r\n', '')
	print "Texto Limpiado: ",limpio
	print "ENVIANDO A GENERADOR..."
	crear_archivo(cadena)
	print "Archivo con Texto Creado .. OK"
	generar_arboles()
	print "Arboles Generados .. OK"
	listaObjetos = leerArboles()
	print "Arboles Leidos .. OK"
	#os.popen('echo '+pal+'| analyze -f am.cfg').read()[:-1]
	#stemm = os.popen('php stemm_es.php "'+pal+'"').read()
	return listaObjetos
 
def leerArboles():
	stanford_bikel=[]
	print "Leyendo Arboles..."
	stanford_tree = open("../Arboles_Ptb/arbol-stanford", 'r')
	stanford_string = stanford_tree.read()
	stanford_tree.close()
	stanford_bikel.append(stanford_string)
	bikel_tree = open("../Arboles_Bikel/salida-bikel.parsed", 'r')
	bikel_string = bikel_tree.read()
	bikel_tree.close()
	stanford_bikel.append(bikel_string)
	return stanford_bikel

@app.route('/train')
def info():
	print "ENTRON EN GET INFO"

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=12345, use_reloader=True)
