class Laptop():
	"""A simple attempt to model a Hp_Victus."""
	def __init__(self, name, colour):
		"""Initializing name, colour and model attributes."""
		self.name = name
		self.colour = colour
	def get_Speed(self):
		"""Setting the refress rate speed of the Laptop."""
		print("Top refress rate speed of " + self.name + " is 144hz") 

# Creating an instance/object called Hp_Victus
Hp_Victus = Laptop("Hp_Victus","Black")
# Calling the method using the name of the instance
Hp_Victus.get_Speed() 