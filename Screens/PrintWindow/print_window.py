from kivy.uix.screenmanager import Screen
#from Moduls.print import Print
from pyphotonfile import Photon
#import os
#import io
#from PIL import Image
#import numpy as np
import pygame
#from math import *
import math
from kivy.properties import BooleanProperty
import time

class PrintWindow(Screen):
	isShownParams = BooleanProperty(False)

	def select(self, path, filename):

		photon = Photon(filename[0])
		self.isShownParams = BooleanProperty(True)

		weight_g = int(photon.weight_g)
		layer_height = round(photon.layer_height, 2)
		lifting_speed = round(photon.lifting_speed, 2)
		print_time = time.strftime('%H:%M:%S', time.gmtime(photon.print_time))

		model_name = filename[0].rsplit('\\')
		self.ids.model_name.text = str(model_name[-1])
		self.ids.bottom_light.text = str(photon.exposure_time_bottom)
		self.ids.main_light.text = str(photon.exposure_time)
		self.ids.model_weight.text = str(weight_g)
		self.ids.model_thinkness.text = str(layer_height)
		self.ids.printing_time.text = str(print_time)
		self.ids.layers_amount.text = str(photon.n_layers)
		self.ids.lifting_speed.text = str(lifting_speed)

		#im = photon.preview_lowres_data

		prevSurf=self.getPreviewBitmap(photon)
		pygame.image.save(prevSurf, 'Temp/preview.png')
		
		self.ids.model_img.reload()
		self.ids.model_img.source = 'Temp/preview.png'



	def getPreviewBitmap(self, photon):
		""" Decodes a RLE byte array from PhotonFile object to a pygame surface.
		    Based on https://github.com/Reonarudo/pcb2photon/issues/2
		    Encoding scheme:
		        The color (R,G,B) of a pixel spans 2 bytes (little endian) and each color component is 5 bits: RRRRR GGG GG X BBBBB
		        If the X bit is set, then the next 2 bytes (little endian) masked with 0xFFF represents how many more times to repeat that pixel.
		"""

		# Tell PhotonFile we are drawing so GUI can prevent too many calls on getBitmap
		self.isDrawing = True

		# Retrieve resolution of preview image and set pygame surface to that size.
		w = photon.preview_lowres_resolution_x
		h = photon.preview_lowres_resolution_y

		scale = ((1440 / 4) / w, (1440 / 4) / w)
		#scale = ((800 / 2) / w, (600 / 2) / w)
		memory = pygame.Surface((int(w), int(h)))
		if w == 0 or h == 0: return memory # if size is (0,0) we return empty surface

		# Retrieve raw image data and add last byte to complete the byte array
		bA = photon.preview_lowres_data

		# Decode bytes to colors and draw lines of that color on the pygame surface
		idx = 0
		pixelIdx = 0
		while idx < len(bA):
		    # Combine 2 bytes Little Endian so we get RRRRR GGG GG X BBBBB (and advance read byte counter)
		    b12 = bA[idx + 1] << 8 | bA[idx + 0]
		    idx += 2
		    # Retrieve colr components and make pygame color tuple
		    red = math.floor(((b12 >> 11) & 0x1F) / 31 * 255)
		    green = math.floor(((b12 >> 6) & 0x1F) / 31 * 255)
		    blue = math.floor(((b12 >> 0) & 0x1F) / 31 * 255)
		    col = (red, green, blue)

		    # If the X bit is set, then the next 2 bytes (little endian) masked with 0xFFF represents how many more times to repeat that pixel.
		    nr = 1
		    if b12 & 0x20:
		        nr12 = bA[idx + 1] << 8 | bA[idx + 0]
		        idx += 2
		        nr += nr12 & 0x0FFF

		    # Draw (nr) many pixels of the color
		    for i in range(0, nr, 1):
		        x = int((pixelIdx % w))
		        y = int((pixelIdx / w))
		        memory.set_at((x, y), col)
		        pixelIdx += 1

		# Scale the surface to the wanted resolution
		memory = pygame.transform.scale(memory, (int(w * scale[0]), int(h * scale[1])))

		# Done drawing so next caller knows that next call can be made.
		self.isDrawing = False
		return memory

