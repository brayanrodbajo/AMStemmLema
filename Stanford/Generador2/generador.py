#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
#from Generador.test_tree import *
from test_tree import *
reload(sys)  
sys.setdefaultencoding('utf8')

def crear_archivo(texto):
	print "Escribiendo Archivo..."
	fileraw=open("input_text", "w")
	fileraw.write(texto)
	fileraw.close()

def generar_arboles():
	# entrenamiento()
	precarga("input_text")

def train():
	entrenamiento()

import sys
sys.path.insert(0, '../Parseval')
from parseval import *
def do_parseval(n_ptb=1):
	model = Modelo()
	# precarga("../raw_text_Ptb/wsj_000"+str(n_ptb), True) # true para que le quite el root a los arboles de stanford
	print "En DoParseval antes de stanford"
	
	pre_re_st = model.parseval("../Arboles_Stanford/arbol-stanford-"+str(n_ptb), "../Arboles_Ptb/wsj_000"+str(n_ptb)+".mrg")
	pre_re_bi = model.parseval("../Arboles_Bikel/arbol-bikel-"+str(n_ptb)+".parsed", "../Arboles_Ptb/wsj_000"+str(n_ptb)+".mrg")

	print ("PARSEVAL EN GENERADOR \n"+str(pre_re_st)+"\n"+str(pre_re_bi))
	return (pre_re_st,pre_re_bi)

if __name__ == '__main__':
	crear_archivo(sys.argv[1])
	generar_arboles()
