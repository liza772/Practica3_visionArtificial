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