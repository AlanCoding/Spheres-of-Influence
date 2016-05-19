


class Object(object):
	a = 0
	
	def escape_velocity(self):
		return

	def common_ancesstor(self, other):
		return

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
		if isinstance(A, Location)

	def break_into_segments(self):
		common = self.A.common_ancesstor(self.B)

