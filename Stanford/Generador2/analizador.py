# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import os, sys
from generador import *
reload(sys)
sys.setdefaultencoding('utf8')
app = Flask(__name__)

global pre_re_st, pre_re_bi, arbol_stanford_parseval, arbol_bikel_parseval, arbol_ptb, rawtext
@app.route('/')
def cargar():
	global pre_re_st, pre_re_bi, arbol_stanford_parseval, arbol_bikel_parseval, arbol_ptb, rawtext
	print 'Entro en cargar'
	train()
	numero=6
	(pre_re_st,pre_re_bi)=do_parseval(numero)
	stanford_tree = open("../Arboles_Ptb/arbol-stanford", 'r')
	arbol_stanford_parseval = stanford_tree.read()
	stanford_tree.close()
	bikel_tree = open("../Arboles_Bikel/salida-bikel.parsed", 'r')
	arbol_bikel_parseval = bikel_tree.read()
	bikel_tree.close()
	ptb = open("../Arboles_Ptb/wsj_000"+str(numero)+".mrg", 'r')
	arbol_ptb = ptb.read()
	ptb.close()
	r_file = open("../raw_text_Ptb/wsj_000"+str(numero), 'r')
	rawtext = r_file.read()
	r_file.close()
	return render_template('index.html', result_precision_bikel=str(pre_re_bi[0]), result_recall_bikel=str(pre_re_bi[1]), result_precision_stanford=str(pre_re_st[0]),  result_recall_stanford=str(pre_re_st[1]), arbol_bikel_parseval=arbol_bikel_parseval, arbol_stanford_parseval=arbol_stanford_parseval, arbol_ptb=arbol_ptb, rawtext=rawtext)
	
# @app.route('/parseval')
# def parseval():
# 	parseval=do_parseval()
# 	return render_template('index.html', result_precision_stanford=str(parseval[0]),  result_recall_stanford=str(parseval[1]))

@app.route('/', methods=['POST'])
def obtener(): 
	global pre_re_st, pre_re_bi
	print "ENTRO en obtener"
	#os.system('analyze -f /usr/local/share/freeling/config/es.cfg tagged < /var/www/html/input.txt > /var/www/html/output.txt')
	texto=str(request.form['id_entrada'])
	print ("Texto Recibido: ", texto)
	trees=["a","b"]
	trees=crear_arboles(texto)
	#print(analisis_morfo)
	return render_template('index.html', texto=texto, tr_stanford=trees[0], tr_bikel=trees[1], result_precision_bikel=str(pre_re_bi[0]), result_recall_bikel=str(pre_re_bi[1]), result_precision_stanford=str(pre_re_st[0]),  result_recall_stanford=str(pre_re_st[1]), arbol_bikel_parseval=arbol_bikel_parseval, arbol_stanford_parseval=arbol_stanford_parseval, arbol_ptb=arbol_ptb, rawtext=rawtext)

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


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=12345, use_reloader=True)
