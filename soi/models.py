
def common_ancesstor(o1, o2):
	return



class Object(object):
	a = 0
	parent = None
	data = None

	def __init__(self, parent, data):
		self.name = data.get('name', None)
		self.data = data
		if self.is_apex():
			return
		if not parent:
			raise Exception('No parent provided for planet or moon')

	def escape_velocity(self):
		return

	def ancesstor_list(self):
		ret = []
		obj = self
		while True:
			if obj.parent is None:
				return ret
			obj = obj.parent
			ret.append(obj)

	def is_apex(self):
		if self.name is None:
			raise Exception('null name: ' + str(self.data))
		return (self.name.lower() == 'sun' or self.name.lower() == 'kerbol')

class System(object):
	objects = {}
	
	def __init__(self, name='Sun'):
		sun_obj = Object(None, data={
			'name': name,
			'a': 0., 'i': 0., 'r': 0., 'albedo': 0.99,
		})
		self.name = name
		sun_obj.name = name
		sun_obj.data['name'] = name
		self.objects[name] = sun_obj

	def add_data(self, data):
		# list of planets
		if isinstance(data, list):
			for planet in data:
				obj = Object('Sun', planet)
				self.objects[planet['name']] = obj
		# list of moons
		elif isinstance(data, dict):
			for planet in data:
				for moon in data[planet]:
					obj = Object(planet, data[planet][moon])
					self.objects[moon] = obj
		else:
			raise Exception('Bad input data')
		self.build_parents()

	def build_parents(self):
		for name in self.objects:
			obj = self.objects[name]
			if obj.is_apex():
				continue
			if not obj.parent:
				parent_name = obj.data['parent']
				obj.parent = self.objects[parent_name]
				
			

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

