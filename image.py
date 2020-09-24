# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:19:14 2020

@author: rick-
"""

from matplotlib import pyplot as plt #Libreria de graficos
from PIL import Image  #Libreria para abrir una imagen
import time  #Libreria para medir el tiempo
import numpy as np
#from matplotlib.pyplot import plot

def abrir_imagen(im):
    tiempoIn = time.time()  #Inicio del contador de tiempo
    ruta = ('C:/Users/rick-/OneDrive/Documentos/Python/Imagenes/' + im) #Carga de ruta de imagen
    im = Image.open(ruta)   #Cargamos imagen
    im.show()   #Visualizamos imagen
    tiempoFin = time.time() 
    print('El proceso tardo {}[s]'.format(tiempoIn-tiempoFin))
    print(im.format, im.size, im.mode)  #Formato, Tamaño y banda de la imagen
    

def escala_grises(im):
    image = Image.open(im) #Forma corta
    image.show()
    
    im2 = image #Guardamos la imagen original
    i = 0
    
    #Obtencion de los pixeles de la imagen
    while i < im2.size[0]:  #Renglones
        j = 0
        while j < im2.size[1]:  #Columnas
            r, g, b = im2.getpixel((i,j)) #Optencion de los pixeles de RGB
            g = (r + g + b) / 3 #Escala de grises con el promedio de la escala RGB
            gris = int(g)   #convercion de float a int
            pixel = tuple([gris, gris, gris])   #contiene la escala de grises
            im2.putpixel((i,j), pixel)  #ingresa los pixeles a la imagen original
            j += 1
        i += 1
    im2.show()
    
def max_gris(im):
    image = Image.open(im)
    image.show()
    
    im3 = image #Guardamos la imagen original
    i = 0
    
    #Obtencion de los pixeles de la imagen
    while i < im3.size[0]:  #Renglones
        j = 0
        while j < im3.size[1]:  #Columnas
            maximo = max(im3.getpixel((i,j)))   #Pixel maximo de la imagen
            #Nivel maximo de toda la escala de grises usando el pixel maximo
            pixel = tuple([maximo, maximo, maximo])
            im3.putpixel((i,j),pixel)
            j+=1
        i+=1
    print('El nivel maximo es: {}'.format(maximo))
    im3.show()

def min_gris(im):
    image = Image.open(im)
    image.show()
    
    im4 = image #Guardamos la imagen original
    i = 0
    
    #Obtencion de los pixeles de la imagen
    while i < im4.size[0]:  #Renglones
        j = 0
        while j < im4.size[1]:  #Columnas
            minimo = min(im4.getpixel((i,j)))   #Pixel minimo de la imagen
            #Nivel minimo de toda la escala de grises usando el pixel minimo
            pixel = tuple([minimo, minimo, minimo])
            im4.putpixel((i,j),pixel)
            j+=1
        i+=1
    print('El nivel minimo es: {}'.format(minimo))
    im4.show()
    
def negativo(im):
    image = Image.open(im)
    image.show()
    
    im5 = image #Guardamos la imagen original
    i = 0
    
    #Obtencion de los pixeles de la imagen
    while i < im5.size[0]:  #Renglones
        j = 0
        while j < im5.size[1]:  #Columnas
            r, g, b = im5.getpixel((i,j))
            #Negativo
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b
            pixel = tuple([rn, gn, bn])
            im5.putpixel((i,j), pixel)
            j+=1
        i+=1
    im5.show()

def neg_gris(im):
    image = Image.open(im)
    image.show()
    print(image.mode)
    
    im6 = image #Guardamos la imagen original
    i = 0
    
    #Obtencion de los pixeles de la imagen
    while i < im6.size[0]:  #Renglones
        j = 0
        while j < im6.size[1]:  #Columnas
            gris = im6.getpixel((i,j))
            #Negativo
            gn = 255 - gris
            im6.putpixel((i,j), gn)
            j+=1
        i+=1
    im6.show()
    
def b_n(im, grisBase):
    image = Image.open(im)
    image.show()
    
    im7 = image #Guardamos la imagen original
    i = 0
    
    #Obtencion de los pixeles de la imagen
    while i < im7.size[0]:  #Renglones
        j = 0
        while j < im7.size[1]:  #Columnas
            r,g,b = im7.getpixel((i,j))
            gris = (r+ g+ b) / 3
            if gris < grisBase:
                im7.putpixel((i,j), (0,0,0))
            else:
                im7.putpixel((i,j), (255,255,255))
            j += 1
        i += 1
    im7.show()
    
def tran_im(im):
    image = Image.open(im)
    image.show()
    
    im8 = image #Guardamos la imagen original
    ar = np.zeros((im8.size[0], im8.size[1]))    #matriz de ceros del tamaño de la imagen
    i = 0
    
    #Obtencion de los pixeles de la imagen
    while i < im8.size[1]:  #Columnas
        j = 0
        while j < im8.size[0]:  #Renglones
            a = im8.getpixel((j,i))
            ar[j, i] = a
            j += 1
        i += 1
    ar = ar.astype(int)
    im8 = Image.fromarray(ar)
    im8.show()
    
def histograma(im):
    
    image = Image.open(im).convert('L') #Convertimos imagen a escala de grises
    image.show()
    
    im9 = image
    [ren, col] = im9.size
    total = ren * col
    a = np.asanyarray(im9, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)
    valor = 0
    maxd = max(a)
    grises = maxd
    vec = np.zeros(grises + 1)
    for i in range(total - 1):
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.plot(vec)
    
def brillo(im):
    image = Image.open(im).convert('L') #Convertimos imagen a escala de grises
    image.show()
    
    im10 = image
    
    arr = np.array(im10.size)
    total = arr[0] * arr[1]
    i = 0
    suma = 0
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            suma = suma + im10.getpixel((i,j))
            j += 1
        i += 1
    brillo = suma / total
    brillo = int(brillo)
    print('El brillo de la images es: {}'.format(brillo))
    
def contraste(im):
    image = Image.open(im).convert('L') #Convertimos imagen a escala de grises
    image.show()
    
    im11 = image
    
    arr = np.array(im11.size)
    total = arr[0] * arr[1]
    i = 0
    suma = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            suma = suma + im11.getpixel((i,j))
            j += 1
        i += 1
    brillo = suma / total
    
    #Aplicaciondel contraste
    while i < im11.size[0]:
        while j < im11.size[1]:
            aux = im11.getpixel((i,j))-brillo
            suma = suma + aux
            j +=1
        i += 1
    cont = suma * suma
    cont = np.sqrt(suma / total)
    contraste_ = int(cont)
    print('El contraste de la imagen es: {}'.format(contraste_))

def suma_im(im, alpha):
    image = Image.open(im).convert('L') #Convertimos imagen a escala de grises
    image.show()
    
    im12 = image
    
    i = 0
    while i < im12.size[0]:
        j = 0
        while j < im12.size[1]:
            val = im12.getpixel((i,j))
            val = val + alpha
            if val <= 0:
                val = abs(val)
            else:
                val = val
            im12.putpixel((i,j),val)
            j += 1
        i += 1
    im12.show()
    
def res_im(im, alpha):
    image = Image.open(im).convert('L') #Convertimos imagen a escala de grises
    image.show()
    
    im12 = image
    
    i = 0
    while i < im12.size[0]:
        j = 0
        while j < im12.size[1]:
            val = im12.getpixel((i,j))
            val = val - alpha
            if val >=255:
                val = 255
            else:
                val = val
            im12.putpixel((i,j),val)
            j += 1
        i += 1
    im12.show()        

def mult_im(im, alpha):
    image = Image.open(im).convert('L') #Convertimos imagen a escala de grises
    image.show()
    
    im12 = image
    
    i = 0
    while i < im12.size[0]:
        j = 0
        while j < im12.size[1]:
            val = im12.getpixel((i,j))
            val = val * alpha
            if val >=255:
                val = 255
            else:
                val = val
            im12.putpixel((i,j),val)
            j += 1
        i += 1
    im12.show()   

def div_im(im, alpha):
    image = Image.open(im).convert('L') #Convertimos imagen a escala de grises
    image.show()
    
    im12 = image
    
    i = 0
    while i < im12.size[0]:
        j = 0
        while j < im12.size[1]:
            val = im12.getpixel((i,j))
            val = val / alpha
            val = int(val)
            if val <= 0:
                val = abs(val)
            else:
                val = val
            im12.putpixel((i,j),val)
            j += 1
        i += 1
    im12.show()   

#abrir_imagen('torax.jpg')   #cargamos imagen
#escala_grises('test_2.jpg')
#max_gris('test_2.jpg')
#min_gris('test_2.jpg')
#negativo('test.png')
#neg_gris('test_3.jpg')
#b_n('torax.jpg', 100)
#tran_im('test_2.jpg')
#histograma('test_2.jpg')
#brillo('test_2.jpg')
#contraste('test_2.jpg')
#suma_im('test_2.jpg', 50)
#res_im('test_2.jpg', 50)
#mult_im('test_2.jpg', 50)
#div_im('test_2.jpg', 50)

