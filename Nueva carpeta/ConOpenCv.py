# -*- coding: utf-8 -*-
#importamos openCv
import cv2 
#importamos Tkinter para interfaz
from Tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw() #Dibuja Interfaz Tk para elegir archivo  
filename = askopenfilename() #Metodo para poder elegir un archivo del sistema *FileChooser* 
img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)#Se debe configurar aqui ,IMREAD_UNCHANGED de openCv devuelve la img sin ningun cambio

scale_percent = input("ingresa porcentaje %: ") # ingresa valor / o poner estatico
width = int(img.shape[1] * scale_percent / 100)#shape devuelve el valor de una matriz 0 para columnas 1 para filas
height = int(img.shape[0] * scale_percent / 100)

dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)# INTER_AREA reduce por medio de los pixeles las dimenciones pasadas por los argumentos de resize 

#print('Resized Dimensions : ',resized.shape)
nombre = raw_input("nombra a tu imagen: ") #pide un parametro 
quality = input("cuanta calidad quieres conservar en tu imagen (elige del 0 - 100): ") #pide un parametro 
status = cv2.imwrite(nombre+'.jpg',resized, [cv2.IMWRITE_JPEG_QUALITY, quality])#IMWRITE_JPEG_QUALITY.el ultimo argumento aplica la mayor calidad aplicada (se puede modificar)

cv2.imshow("Imagen ", resized) #se usa para mostrar la imagen en una ventana que openCv preecarga
cv2.waitKey(0) #se usa para introducir un retraso de n milisegundos mientras se procesan imágenes en Windows.
#waitKey(0), devuelve la tecla presionada por el usuario en la ventana activa
cv2.destroyAllWindows()

