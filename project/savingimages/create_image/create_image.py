import os
import random
import matplotlib 

from savingimages.models import Plot
from io import StringIO, BytesIO
from django.core.files import File

# http://stackoverflow.com/questions/27147300/how-to-clean-images-in-python-django
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import time


# http://stackoverflow.com/questions/20580179/saving-a-matplotlib-graph-as-an-image-field-in-database

"""
def criaImagem():
	x = random.sample(range(1,9), 3)
	y = random.sample(range(1,9), 3)
	plt.axis([0, 10, 0, 10])
	plt.plot(x, y, 'o')

	figfile = BytesIO()

	import base64
	
	plt.savefig(figfile, format="png")
	plt.close()
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	return figdata_png
"""

def dynamic_name_image():
	return 'name_of_image' + str(time.time()).replace('.','_') + '.png'

def create_image():
	x = random.sample(range(1,9), 3)
	y = random.sample(range(1,9), 3)
	plt.axis([0, 10, 0, 10])
	plt.plot(x, y, 'o')

	f = BytesIO()
	plt.savefig(f, format="png")

	content_file = File(f)
	model_object = Plot()
	model_object.image.save(dynamic_name_image(), content_file)
	model_object.save()
	plt.close()











"""
def criaImagem(path, image_name):
	x = random.sample(range(1,9), 3)
	y = random.sample(range(1,9), 3)

	plt.axis([0, 10, 0, 10])
	plt.plot(x, y, 'o')
	# Truque para mudar o lugar onde a figura será criada.
	initial_path = os.getcwd()
	os.chdir(path)
	plt.savefig(image_name)
	plt.close()
	# Não sei se é realmente necessario voltar ao diretório atual.
	os.chdir(initial_path) 
"""	