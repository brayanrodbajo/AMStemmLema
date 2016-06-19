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
	entrenamiento()
	precarga("input_text")

if __name__ == '__main__':
	crear_archivo(sys.argv[1])
	generar_arboles()
