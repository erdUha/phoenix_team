from django.shortcuts import render
from main.models import Phones
from django.http import HttpResponseRedirect
from django.urls import resolve
# Create your views here.

def index(request): # Главная старница
	return render(request, 'aituc_po2201/main.html')

def catalog(request): # Вывод каталога
	data = Phones.objects.all()
	field_value = []
	for dat in data: # Создание словаря из информации о смартфонах
		img = getattr(dat, Phones._meta.get_field('img').attname)
		if img.find('//static.shop.kz') == -1:
			img = '//static.shop.kz' + img
		field_value.append({
			'uuid': getattr(dat, Phones._meta.get_field('uuid').attname),
			'name': getattr(dat, Phones._meta.get_field('name').attname),
			'cost': getattr(dat, Phones._meta.get_field('cost').attname),
			'bad_cost': getattr(dat, Phones._meta.get_field('bad_cost').attname),
			'color': getattr(dat, Phones._meta.get_field('color').attname),
			'screen_size': getattr(dat, Phones._meta.get_field('screen_size').attname),
			'screen_dimensions': getattr(dat, Phones._meta.get_field('screen_dimensions').attname),
			'matrix_type': getattr(dat, Phones._meta.get_field('matrix_type').attname),
			'max_brightness': getattr(dat, Phones._meta.get_field('max_brightness').attname),
			'frequency': getattr(dat, Phones._meta.get_field('frequency').attname),
			'glass': getattr(dat, Phones._meta.get_field('glass').attname),
			'ram': getattr(dat, Phones._meta.get_field('ram').attname),
			'storage': getattr(dat, Phones._meta.get_field('storage').attname),
			'cpu': getattr(dat, Phones._meta.get_field('cpu').attname),
			'cores': getattr(dat, Phones._meta.get_field('cores').attname),
			'cpu_frequency': getattr(dat, Phones._meta.get_field('cpu_frequency').attname),
			'main_camera': getattr(dat, Phones._meta.get_field('main_camera').attname),
			'front_camera': getattr(dat, Phones._meta.get_field('front_camera').attname),
			'video': getattr(dat, Phones._meta.get_field('video').attname),
			'sims': getattr(dat, Phones._meta.get_field('sims').attname),
			'sim_type': getattr(dat, Phones._meta.get_field('sim_type').attname),
			'battery': getattr(dat, Phones._meta.get_field('battery').attname),
			'android': getattr(dat, Phones._meta.get_field('android').attname),
			'warranty': getattr(dat, Phones._meta.get_field('warranty').attname),
			'img': img,
		})
	return render(request, 'aituc_po2201/catalog.html', {'phones': field_value,}) 

def page(request):
	uuid = request.path[9:-1]
	data = Phones.objects.get(uuid=uuid)
	print('YOURMOM ' + str(data))
	img = getattr(data, Phones._meta.get_field('img').attname)
	if img.find('//static.shop.kz') == -1:
		img = '//static.shop.kz' + img
	field_value = {
		'uuid': getattr(data, Phones._meta.get_field('uuid').attname),
		'name': getattr(data, Phones._meta.get_field('name').attname),
		'cost': getattr(data, Phones._meta.get_field('cost').attname),
		'bad_cost': getattr(data, Phones._meta.get_field('bad_cost').attname),
		'color': getattr(data, Phones._meta.get_field('color').attname),
		'screen_size': getattr(data, Phones._meta.get_field('screen_size').attname),
		'screen_dimensions': getattr(data, Phones._meta.get_field('screen_dimensions').attname),
		'matrix_type': getattr(data, Phones._meta.get_field('matrix_type').attname),
		'max_brightness': getattr(data, Phones._meta.get_field('max_brightness').attname),
		'frequency': getattr(data, Phones._meta.get_field('frequency').attname),
		'glass': getattr(data, Phones._meta.get_field('glass').attname),
		'ram': getattr(data, Phones._meta.get_field('ram').attname),
		'storage': getattr(data, Phones._meta.get_field('storage').attname),
		'cpu': getattr(data, Phones._meta.get_field('cpu').attname),
		'cores': getattr(data, Phones._meta.get_field('cores').attname),
		'cpu_frequency': getattr(data, Phones._meta.get_field('cpu_frequency').attname),
		'main_camera': getattr(data, Phones._meta.get_field('main_camera').attname),
		'front_camera': getattr(data, Phones._meta.get_field('front_camera').attname),
		'video': getattr(data, Phones._meta.get_field('video').attname),
		'sims': getattr(data, Phones._meta.get_field('sims').attname),
		'sim_type': getattr(data, Phones._meta.get_field('sim_type').attname),
		'battery': getattr(data, Phones._meta.get_field('battery').attname),
		'android': getattr(data, Phones._meta.get_field('android').attname),
		'warranty': getattr(data, Phones._meta.get_field('warranty').attname),
		'img': img,
	}
	return render(request, 'aituc_po2201/product.html', {'phone': field_value,}) # Вывод странички

def cart(request):
	return render(request, 'aituc_po2201/cart.html')
