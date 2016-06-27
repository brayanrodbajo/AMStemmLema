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
oraciones=[]

# corenlp_dir = "../stanford-corenlp-full-2014-08-27/"
# coreStanfordNLP = StanfordCoreNLP(corenlp_dir)


def entrenamiento():
	global coreStanfordNLP
	print "Empezando Entrenamiento..."
	corenlp_dir = "../stanford-corenlp-full-2014-08-27/"
	coreStanfordNLP = StanfordCoreNLP(corenlp_dir)
	print "Fin Entrenamiento"

def precarga(archivo, numero):
	


	global oraciones
	print "Leyendo el archivo..."
	fileraw = open(archivo, 'r')
	oraciones=[]
	textoraw = fileraw.read()
	# limpio = textoraw.replace('\r\n', ' ')	
	limpio = textoraw.replace('.START', '')
	# limpio = limpio.replace('\n', '')
	limpio = limpio.replace(' \n\n', ' ') 
	sents = sent_tokenize(limpio)
	oraciones=sents
	fileraw.close()
	# print oraciones
	create_tree(numero)



def create_tree(numero):#parseval = true si se requiere quitar el ROOT del stanford para comparar con PTB por parseval
	global oraciones, coreStanfordNLP
	print "Creando Arbol..."
	#open('../Arboles_Bikel/salida-bikel', 'w').close() #Se limpia el archivo para solo guardar las oraciones que pertenecen a la anterior entrada.
	whole_tree= ""
	for oracion in oraciones:
		stanford_parse=coreStanfordNLP.parse(oracion)
		listas=json.loads(stanford_parse)
		if "(ROOT" in  stanford_parse:
			stanford_parse = stanford_parse[stanford_parse.index("(ROOT"):stanford_parse.rindex(")")+1]
		stanford_parse="( "+stanford_parse[6:-1]+" )" #quita el ROOT de cada oracion y agrega un paréntesis
		whole_tree+=stanford_parse+"\n"
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
		armarBikel(pal,tag, numero)
	arbolBikel(numero)
	arbol=open("../Arboles_Stanford/arbol-stanford-"+str(numero), "w")
	arbol.write(whole_tree)
	arbol.close()

def armarBikel(palabras, tags, numero):
	print "Preprocesando Bikel..."
	bikel=""
	i=0
	for p in palabras:
		bikel+="("+p+" "+"("+tags[i]+"))"
		i+=1
	bikel="("+bikel+")"
	#print "BIKEL \n",bikel
	f=open("../Arboles_Bikel/arbol-bikel-"+str(numero), "a")
	f.write(bikel+"\n")
	f.close()
	

def arbolBikel(numero):
	print "Creando Arbol de Bikel"
	os.system("./../../Bikel/dbparser/bin/parse 400 ../../Bikel/dbparser/settings/collins.properties ../../Bikel/wsj-02-21.obj.gz ../Arboles_Bikel/arbol-bikel-"+str(numero))
	# analizar_arbol("../Stanford/salida-bikel.parsed", "wsj_0001.mrg")

def analizar_arbol(arbol1, arbol2):
	Modelo.parseval(arbol1, arbol2)
	print "EXITO :)"

if __name__ == '__main__':
	entrenamiento()
	for i in range(5,100):
		if(i>=10):
			path="../raw_text_Ptb/wsj_00"+str(i)
		else:
			path="../raw_text_Ptb/wsj_000"+str(i)
		print "Enviando: ",path
		precarga(path, i)
	# analizar_arbol("../Stanford/salida-bikel.parsed", "../wsj_0001.mrg")
