from flask import Flask, request, render_template
#from flask import render_template
import os
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
	analisis_morfo=	ejecutarAnal(texto)
	print(analisis_morfo)
	return render_template('index.html', texto=texto, texto_analisis=analisis_morfo)

def ejecutarAnal(cadena):
	# file=open("entrada.txt", "w")
	# file.write(cadena)
	# file.close()
	palabras = cadena.split(' ')
	txt_analizado =""
	for pal in palabras:
		txt_analizado += os.popen('echo '+pal+'| analyze -f am.cfg').read()[:-1]
		txt_analizado += os.popen('php stemm_es.php "'+pal+'"').read()
		txt_analizado += '\n'
	return txt_analizado

# def leerArchivo():
# 	file=open("salida.txt", "r")
# 	morfo=""
# 	for line in file:		
# 		morfo+=line
# 	return morfo


if __name__ == '__main__': 
	app.run()
