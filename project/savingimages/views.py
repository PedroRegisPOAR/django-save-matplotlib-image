from django.shortcuts import render

# This name is ogly, but I don't know a better way to do this.
from savingimages.create_image.create_image import create_image
from . models import Plot


def home(request):
	return render(request, 'savingimages/home.html')


def create_image_and_show(request):
	
	#	http://stackoverflow.com/questions/11456410/image-file-not-deleted-when-object-with-imagefield-field-is-deleted
	for plt in Plot.objects.all():
		plt.delete()

	create_image()

	#	http://stackoverflow.com/questions/1256190/django-getting-last-object-created-simultaneous-filters
	last_plot = Plot.objects.latest('id')
	context = {'last_plot':last_plot}

	return render(request,'savingimages/mytemplate.html', context)

	#	https://timmyomahony.com/blog/static-vs-media-and-root-vs-path-in-django/