from PIL import Image
from PIL.ExifTags import TAGS
def getMetaData(): #Metodo para obtener los metadatos
		imgname = input("Ingresa el nombre de la imagen (JPG): ")
		out = input("Ingresa el nombre del txt: ")

		try:
				metaData = {}

				imgFile = Image.open(imgname) #Se abre el archivo de la imagen
				print ("Obteniendo los metadatos...")
				info = imgFile._getexif() #Se obtienen los metadatos
				if info: # Si se encuentra la informacion
						print ("Encontro los metadatos!")
						for (tag, value) in info.items(): #Se inicia un ciclo para obtener los datos y se guardan en la variable que se establecio previamente 
								tagname = TAGS.get(tag, tag)
								metaData[tagname] = value
								if not out:
										print (tagname, value)
						if out: #Una vez que finaliza se genera el archivo
								print ("Generando el archivo...")
								with open(out,'w') as f: #Se crea el archivo y se establece en modo escritura con la w
										for (tagname, value) in metaData.items():#Mediante el ciclo se escriben los datos obtenidos en el archivo de texto
												f.write(str(tagname)+"\t"+\
														str(value)+"\n")
								return 1 #Regresa un 1 para saber si termino el proceso de forma exitosa
				else:
					print("No funciona")
		except:
				print ("Failed")

if __name__ == '__main__': 
    getMetaData()
	#app.run(debug=True, port=4000)
	