import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
from numpy.core.fromnumeric import size #Opencv

from skimage import io

import imutils
from PIL import ImageTk
from PIL import Image as Im
fila = 4
columna = 3

#Imágenes Iniciales
img1 = cv2.imread('floramarilla.png', 1)
img2 = cv2.imread('florazul.png', 1)

#Dimencionamiento en bruto
Redimg1 = cv2.resize(img1, (300, 200))
Redimg2 = cv2.resize(img2, (300, 200))

#De matriz BGR a RGB
Redimg1 = cv2.cvtColor(Redimg1, cv2.COLOR_BGR2RGB)
Redimg2 = cv2.cvtColor(Redimg2, cv2.COLOR_BGR2RGB)



operacion="Suma"
Redimgop=cv2.add(Redimg1,Redimg2)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Resta"
Redimgop=cv2.subtract(Redimg1,Redimg2)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Multiplicacion"
Redimgop=cv2.multiply(Redimg1,Redimg2)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Division"
Redimgop=cv2.divide(Redimg1,Redimg2)
graficar(operacion,Redimg1,Redimg2,Redimgop)
operacion="Raiz cuadrada"
Redimgop=Redimg1
Redimgop=np.sqrt(Redimgop)
Redimgop=np.asarray(Redimgop, dtype = int)
cv2.imwrite("resultSQRT.jpg",Redimgop)
Redimgop = cv2.imread('resultSQRT.jpg', 1)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Potencia"
Redimgop=Redimg1
Redimgop=np.power(Redimgop,2)
Redimgop=np.asarray(Redimgop, dtype = int)
cv2.imwrite("resultPower.jpg",Redimgop)
Redimgop = cv2.imread('resultPower.jpg', 1)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Conjuncion"
Redimgop=cv2.bitwise_and(Redimg1,Redimg2)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Disyuncion"
Redimgop=cv2.bitwise_or(Redimg1,Redimg2)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Negacion"
Redimgop=Redimg1
Redimgop=image= 255-Redimgop
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Translacion"
ancho = Redimg1.shape[1] #columnas
alto = Redimg1.shape[0] #fila
M = np.float32([[1,0,2],[0,1,2]])
Redimgop = cv2.warpAffine(img1,M,(ancho,alto))
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Escalado"
Redimgop= imutils.resize(Redimg1,height=400)
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()
operacion="Rotacion"
ancho = Redimg1.shape[1] #columnas
alto = Redimg1.shape[0] #fila
M = cv2.getRotationMatrix2D((ancho//2,alto//2),15,1)
Redimgop = cv2.warpAffine(img1,M,(ancho,alto))
graficar(operacion,Redimg1,Redimg2,Redimgop)
plt.close()