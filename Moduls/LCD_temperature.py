class LCDTemperature():

	def get_out_temp():
		t = range(45, 60)
		temp_out = str(t) + 'C°'
		return temp_out

	lcd_temperature = get_out_temp()