
def common_ancesstor(o1, o2):
	return



class Object(object):
	a = 0
	parent = None

	def __init__(self, data):
		name = data.get('name', None)
		if name.lower() == 'sun' or name.lower() == 'kerbol':
			return

	def escape_velocity(self):
		return

	def ancesstor_list(self):
		while True:
			break


class System(object):
	objects = {}

	def add_data(self, data):
		if isinstance(data, list):
			for planet in data:
				self.objects[planet['name']] = planet
		elif isinstance(data, dict):
			for planet in data:
				for moon in data[planet]:
					self.objects[moon] = data[planet][moon]
		else:
			raise Exception('Bad input data')

class Location(object):
	object = None
	
	def __init__(self, object, **data):
		self.object = object
		if 'a' in data:
			self.a = data['a']

class Segment(object):
	pass

class Trip(object):
	A = None
	B = None
	
	def __init__(self, A, B):
		if isinstance(A, Location):
			pass

	def break_into_segments(self):
		common = common_ancesstor(self.A, self.B)

