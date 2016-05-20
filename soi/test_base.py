import pytest

from soi.models import *

kerbol_system = [
	{'name': 'Kerbin', 'parent': 'Kerbol'},
	{'name': 'Mun',    'parent': 'Kerbin'},
	{'name': 'Jool',   'parent': 'Kerbol'}
]

def test_ancestry_list():
	obj = Object(kerbol_system[1])
	
	assert False