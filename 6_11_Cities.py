citites = {'Pensacola': {'Country': 'United States', 'Population': '53,678' , 'Fact': 'Home to Pensacola beach'}, 
'Houston': {'Country': 'United States', 'Population':'2.288 million' , 'Fact': 'Home to the houston Rockets'}, 
'Las Vegas': {'Country': 'United States', 'Population': '646,790' , 'Fact': 'Home to the las vegas Aces'},}

for city, infomation in citites.items():
	print(f"\nCity: {city}")
	info = f"\n{infomation['Population']} {infomation['Fact']}"
	country = infomation['Country']

	print(f"\nCountry: {country}")
	print(f"\nInfomation: {info}")
