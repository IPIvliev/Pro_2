from kivy.uix.screenmanager import Screen
import configparser

class DeveloperWindow(Screen):

	def save_params(self):
		vat_speed = self.ids.vat_speed_input.text
		vat_amount = self.ids.vat_amount_input.text
		vat_door_speed = self.ids.door_speed_input.text
		vat_lift_distance = self.ids.lift_distance_input.text
		vat_z_step_mm = self.ids.z_step_mm_input.text
		vat_vat_delay = self.ids.vat_delay_input.text
		vat_vat_z_delay = self.ids.vat_z_delay_input.text
		vat_tenzo_weight = self.ids.tenzo_weight_input.text

		config = configparser.ConfigParser()
		config.read('printer_config.ini')
		config_file = open('printer_config.ini', 'w')
		

		config.set("DEFAULT", "vat_speed", vat_speed)
		config.set("DEFAULT", "vat_amount", vat_amount)
		config.set("DEFAULT", "door_speed", door_speed)
		config.set("DEFAULT", "lift_distance", lift_distance)
		config.set("DEFAULT", "z_step_mm", z_step_mm)
		config.set("DEFAULT", "vat_delay", vat_delay)
		config.set("DEFAULT", "vat_z_delay", vat_z_delay)
		config.set("DEFAULT", "tenzo_weight", tenzo_weight)

		config.write(config_file)

		config_file.close()
