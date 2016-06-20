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
def do_parseval():
	model = Modelo()
	precarga("../raw_text_Ptb/wsj_0001")
	pre_re = model.parseval("../Arboles_Ptb/arbol-stanford", "../Arboles_Ptb/wsj_0001.mrg")
	"../Arboles_Bikel/salida-bikel.parsed"
	print (pre_re)
	return pre_re

if __name__ == '__main__':
	crear_archivo(sys.argv[1])
	generar_arboles()
