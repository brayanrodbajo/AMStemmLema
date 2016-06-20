#!/usr/bin/env python
# -*- coding: utf-8 -*-
from corenlp import StanfordCoreNLP
import json
import sys, os
from nltk import tokenize
from nltk.tokenize import sent_tokenize

reload(sys)  
sys.setdefaultencoding('utf8')
global oraciones,coreStanfordNLP

# corenlp_dir = "../stanford-corenlp-full-2014-08-27/"
# coreStanfordNLP = StanfordCoreNLP(corenlp_dir)


def entrenamiento():
	global coreStanfordNLP
	print "Empezando Entrenamiento..."
	corenlp_dir = "../stanford-corenlp-full-2014-08-27/"
	coreStanfordNLP = StanfordCoreNLP(corenlp_dir)
	print "Fin Entrenamiento"

def precarga(archivo):
	global oraciones
	print "Leyendo el archivo..."
	fileraw = open(archivo, 'r')
	oraciones=[]
	textoraw = fileraw.read()
	limpio = textoraw.replace('\r\n', ' ')
	# limpio = limpio.replace('. ', '.')
	# print "Antes de Tokenize: ", limpio
	sents = sent_tokenize(limpio)
	# print "Resultado: ",sents
	# oraciones=limpio.split('.')
	oraciones=sents
	# oraciones.pop()
	# print "MANUAL: ",oraciones
	fileraw.close()
	create_tree()

def create_tree():
	global oraciones, coreStanfordNLP
	print "Creando Arbol..."
	for oracion in oraciones:
		stanford_parse=coreStanfordNLP.parse(oracion)
		listas=json.loads(stanford_parse)
		if "(ROOT" in  stanford_parse:
			stanford_parse = stanford_parse[stanford_parse.index("(ROOT"):stanford_parse.rindex(")")+1]
		arbol=open("../Arboles_Ptb/arbol-stanford", "w")
		arbol.write(stanford_parse+"\n")
		arbol.close()
		pal=[]
		tag=[]
		lista=listas["sentences"][0]["words"]
		#print (lista)
		for word in lista:
			#print word

			pal.append(word[0])
			tag.append(word[1]["PartOfSpeech"])
		#print ("lista de palabras:",pal)
		#print ("lista de tags:",tag)
		armarBikel(pal,tag)
		arbolBikel()

def armarBikel(palabras, tags):
	print "Preprocesando Bikel..."
	bikel=""
	i=0
	for p in palabras:
		bikel+="("+p+" "+"("+tags[i]+"))"
		i+=1
	bikel="("+bikel+")"
	#print "BIKEL \n",bikel
	f=open("../Arboles_Bikel/salida-bikel", "w")
	f.write(bikel+"\n")
	f.close()
	

def arbolBikel():
	print "Creando Arbol de Bikel"
	os.system("./../../Bikel/dbparser/bin/parse 400 ../../Bikel/dbparser/settings/collins.properties ../../Bikel/wsj-02-21.obj.gz ../Arboles_Bikel/salida-bikel")
	# analizar_arbol("../Stanford/salida-bikel.parsed", "wsj_0001.mrg")

def analizar_arbol(arbol1, arbol2):
	Modelo.parseval(arbol1, arbol2)
	print "EXITO :)"

if __name__ == '__main__':
	entrenamiento()
	precarga(sys.argv[1])
	# analizar_arbol("../Stanford/salida-bikel.parsed", "../wsj_0001.mrg")
