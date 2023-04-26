from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Phones(models.Model): # Класс для базы данных, содержащий в себе все данные с парсинга телефонов
	uuid = models.CharField(max_length=255, default='')
	name = models.CharField(max_length=255, default='')
	cost = models.CharField(max_length=255, default='')
	bad_cost = models.CharField(max_length=255, default='')
	color = models.CharField(max_length=255, default='')
	screen_size = models.CharField(max_length=255, default='')
	screen_dimensions = models.CharField(max_length=255, default='')
	matrix_type = models.CharField(max_length=255, default='')
	max_brightness = models.CharField(max_length=255, default='')
	frequency = models.CharField(max_length=255, default='')
	glass = models.CharField(max_length=255, default='')
	ram = models.CharField(max_length=255, default='')
	storage = models.CharField(max_length=255, default='')
	cpu = models.CharField(max_length=255, default='')
	cores = models.CharField(max_length=255, default='')
	cpu_frequency = models.CharField(max_length=255, default='')
	main_camera = models.CharField(max_length=255, default='')
	front_camera = models.CharField(max_length=255, default='')
	video = models.CharField(max_length=255, default='')
	sims = models.CharField(max_length=255, default='')
	sim_type = models.CharField(max_length=255, default='')
	battery = models.CharField(max_length=255, default='')
	android = models.CharField(max_length=255, default='')
	warranty = models.CharField(max_length=255, default='')
	img = models.CharField(max_length=255, default='')
	
