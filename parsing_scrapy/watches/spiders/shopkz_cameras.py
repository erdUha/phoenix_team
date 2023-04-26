import scrapy, uuid

class ShopkzSpider(scrapy.Spider):
	name = 'camera'
	start_urls = ['https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/']
	
	def parse(self, response):
		for link in response.css('div.bx_catalog_item'):
			try:
				product_page = 'https://shop.kz' + link.xpath('.//div[@class="bx_catalog_item_title"]/a').attrib['href']
				
				yield response.follow(product_page, callback=self.parse_item)
				
			except:
				pass
		try:
			next_page = 'https://shop.kz' + response.xpath('//li[@class="bx-pag-next"]/a').attrib['href']
			yield response.follow(next_page, callback=self.parse)
		except:
			pass
	def parse_item(self,response):
		parameters = response.xpath('//div[@class="bx_detail_chars_i"]')
		cost = response.xpath('//span[@class="bx-more-price-text"]/text()')[-1].extract()
		bad_cost = response.xpath('//span[@class="bx-more-price-text"]/text()')[0].extract()
		name = ''
		color = ''
		screen_size = ''
		screen_dimensions = ''
		matrix_type = ''
		frequency = ''
		matrix_dimensions = ''
		matrix_type = ''
		video = ''
		battery = ''
		warranty = ''
		for parameter in parameters:
			if parameter.xpath('.//dt/span/text()').get() == "Производитель":
				name += parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Модель":
				name += ' ' + parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Цвет, используемый в оформлении":
				color += parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Размер экрана, дюйм":
				screen_size = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Разрешение экрана":
				screen_dimensions = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Тип матрицы":
				matrix_type = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Максимальная яркость экрана, кд/м2":
				max_brightness = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Частота обновления экрана, Гц":
				frequency = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Стекло экрана":
				glass = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Объем оперативной памяти":
				ram = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Объем встроенной памяти":
				storage = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Процессор":
				cpu += parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Модель процессора":
				cpu += ' ' + parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Количество ядер":
				cores = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Частота процессора":
				cpu_frequency = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Основная камера, Мп":
				main_camera = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Фронтальная камера, Мп":
				front_camera = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Разрешение видео":
				video = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Количество SIM-карт":
				sims = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Тип SIM-карты":
				sim_type = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Емкость аккумулятора":
				battery = parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Операционная система":
				android += parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Версия ОС на момент начала продаж":
				android += ' ' + parameter.xpath('.//dd/text()').get()
			if parameter.xpath('.//dt/span/text()').get() == "Срок гарантии (мес.)":
				warranty = parameter.xpath('.//dd/text()').get()
		yield {
			'uuid': str(uuid.uuid4()),
			'name': name,
			'cost': cost,
			'bad_cost': bad_cost,
			'color': color,
			'screen_size': screen_size,
			'screen_dimensions': screen_dimensions,
			'matrix_type': matrix_type,
			'max_brightness': max_brightness,
			'frequency': frequency,
			'glass': glass,
			'ram': ram,
			'storage': storage,
			'cpu': cpu,
			'cores': cores,
			'cpu_frequency': cpu_frequency,
			'main_camera': main_camera,
			'front_camera': front_camera,
			'video': video,
			'sims': sims,
			'sim_type': sim_type,
			'battery': battery,
			'android': android,
			'warranty': warranty,
			'img': response.xpath('//span[@class="bx_bigimages_aligner"]/img').attrib['data-src']
		}
