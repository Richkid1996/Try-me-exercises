def car_info(manufacturer, model, **model_info):
	"""Make a dictionary representing a car."""
	car_dict = {
		'manufacturer': manufacturer.title(),
		'model': model.title(),
	}

	for model_info, value in model_info.items():
		car_dict[model_info] = value
	
	return car_dict


my_rangerover = car_info('landrover', 'rangerover', color='blue', interior='tan')
print(my_rangerover)

my_ram = car_info('dodge', 'ram 1500', color='darkgreen', interior='brown')
print(my_ram)

