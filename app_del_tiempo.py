from tkinter import *
import requests 
#86297dad9844c723ccdf4c40f310b5f2
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_respuesta(clima):
	try:
		nombre_ciudad = clima['name']
		desc = clima['weather'][0]['description']
		temp = clima['main']['temp']

		ciudad['text'] = nombre_ciudad
		temperatura['text'] = str(int(temp))+'°C'
		descripcion['text'] = desc
	except:
		ciudad['text'] = 'Ciudad inexistente'


def clima_JSON(ciudad):
	API_KEY = '86297dad9844c723ccdf4c40f310b5f2'
	URL = 'https://api.openweathermap.org/data/2.5/weather'
	parametros = {'APPID':API_KEY, 'q':ciudad, 'units':'metric', 'lang':'es'}
	response = requests.get(URL, params = parametros)
	clima = response.json()
	mostrar_respuesta(clima)
	
		
#PROGRAMA PRINCIPAL
ventana = Tk()
ventana.geometry('350x550')

texto_ciudad = Entry (ventana, font=('Arial',20,'normal'), justify='center')
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana,text='Obtener clima',font=('Arial',10,'bold'),command = lambda:clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font=('Courier',15))
ciudad.pack(padx = 20, pady = 20)

temperatura = Label(font=('Courier',50))
temperatura.pack(padx = 10, pady = 10)

descripcion = Label(font=('Courier',20,'italic'))
descripcion.pack(padx = 10, pady = 10)


ventana.mainloop()