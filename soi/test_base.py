import pytest

from soi.models import *

kerbol_system = [
	{'name': 'Kerbin', 'parent': 'Kerbol'},
	{'name': 'Mun',    'parent': 'Kerbin'},
	{'name': 'Jool',   'parent': 'Kerbol'}
]

@pytest.fixture
def system():
	system = System(name='Kerbol')
	system.add_data(kerbol_system)
	return system

def test_apex():
	obj = Object('Kerbol', {'name': 'Kerbol'})
	assert obj.is_apex()

def test_ancestry_list(system):
	alist = system.objects['Mun'].ancesstor_list()
	
	print(' ancesstor_list: ' + str(alist))
	
	assert alist[0].name == 'Kerbin'
	assert alist[1].name == 'Kerbol'

def test_common_ancestor(system):
	assert system.common_ancesstor('Mun', 'Jool') == 'Kerbol'