from tkinter import *
import math
raiz=Tk()
raiz.title("Calculadora-JDavidYY")
raiz.geometry("400x400")
raiz.config(bg="gray")
miFrame=Frame(raiz)
miFrame.config(width="1000",height="1000")
miFrame.config(bg="brown")
miFrame.pack()
valorContenido=0
operacion=""
agregado=True
resultado=0
#---------------Pantalla-----------------------
numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config( bg="black", fg="pale green", justify="right")

#-------------------Pulsaciones del teclado---------------

def numeroPulsado(num):
	global operacion
	global agregado
	if operacion!="":
		if operacion=="igualdad":
			numeroPantalla.set(num)
			operacion=""
		else:
			if agregado:
				numeroPantalla.set(num)
				agregado=False
			else:
				numeroPantalla.set(numeroPantalla.get()+num)
	else:
		if numeroPantalla.get()=="0":
			numeroPantalla.set(num)
		else:
			numeroPantalla.set(numeroPantalla.get()+num)

#-----------------------Igualdad--------------------------------------

def igual(num):
	global operacion
	global resultado
	global valorContenido
	global agregado
	if operacion=="suma":
		resultado = valorContenido+float(num)
	elif operacion=="resta":
		resultado = valorContenido-float(num)
	elif operacion=="division":
		resultado = valorContenido/float(num)
#-----Suponiengo que desees trabajar la división y la calculadora con números enteros------
#		if resultado-round(resultado)>0.5:
#			resultado = math.ceil(resultado)
#		else:
#			resultado = math.floor(resultado)
	elif operacion =="multiplicacion":
		resultado= valorContenido*float(num)
	operacion="igualdad"
	agregado=True

	numeroPantalla.set(resultado)



#------------------------suma-----------------------

def suma(num):

	global operacion
	global resultado
	global valorContenido
	valorContenido = float(num)
	operacion="suma"

#-----------------------Resta-----------------------------

def resta(num):
	global operacion
	global resultado
	global valorContenido

	valorContenido = float(num)
	operacion="resta"

#-----------------------Division---------------------------

def divide(num):
	global operacion
	global resultado
	global valorContenido
	valorContenido = float(num)
	operacion="division"


#----------------------Multiplicacion---------------------------

def multiplica(num):
	global operacion
	global resultado
	global valorContenido
	valorContenido= float(num)
	operacion = "multiplicacion"


#----------------Fila 1-----------------------------

boton7=Button(miFrame,text="7", width= 5, height= 5, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8", width= 5, height= 5, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9", width= 5, height= 5, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/", width= 5, height= 5, command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=2,column=4)

#----------------------------fila 2--------------------
boton4=Button(miFrame,text="4", width= 5, height= 5, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5", width= 5, height= 5, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6", width= 5, height= 5, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="x", width= 5, height= 5, command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=3,column=4)

#---------------------fila 3-----------------------
boton1=Button(miFrame,text="1", width= 5, height= 5, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width= 5, height= 5, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3", width= 5, height= 5, command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text="-", width= 5, height= 5, command= lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4,column=4)

#---------------------fila 4 ----------------------

boton0=Button(miFrame,text="0", width= 5, height= 5, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",",width= 5, height= 5, command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=", width= 5, height= 5, command=lambda:igual(numeroPantalla.get()))
botonIgual.grid(row=5,column=3)
botonSum=Button(miFrame,text="+",width= 5, height= 5, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5,column=4)
	

raiz.mainloop()
