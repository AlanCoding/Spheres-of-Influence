import re
from copy import copy

planet_list = ['Mercury', 'Venus', 'Earth', 
'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

fancy_planet_list = ['Mercuran', 'Venuian', 'Earth', 
'Martian', 'Jovian', 'Saturnian', 'Uranian', 'Neptunian', 'Pluto']

def parse_val(v):
	pm = '\xc2\xb1'
	v = v.strip('*').replace(',', '')
	if pm in v:
		v = v.split('\xc2\xb1')[0]
	if 'X' in v:
		return 0.5*(float(v.split(' X ')[0]) + float(v.split(' X ')[1]))
	if '-' in v and not v.startswith('-'):
		return 0.5*(float(v.split('-')[0]) + float(v.split('-')[1]))
	if 'Unknown' in v:
		v = 0
	elif 'Yes' in v:
		v = 1
	elif 'No' in v:
		v = 0
	elif v == '?':
		return None
	return float(v)

# Read planet file
with open('data/planets.txt', 'r') as f:
	planet_text = f.read()

planet_dict = {}
for line in planet_text.split('\n'):
	row = re.split(r'\s\t', line)
	if len(planet_dict) == 0:
		for i in range(len(row)):
			planet_dict[i] = {}
			planet_dict[i]['name'] = row[i]
	else:
		if row[0] == 'MOON':
			continue
		for i in range(1, len(row)):
			key = row[0]
			factor = 1
			if key == 'Diameter (km)':
				key = 'dia'
			elif key == 'Distance from Sun (106 km)':
				key = 'a'
				factor = 1.0e6
			elif key == 'Mass (1024kg)':
				key = 'm'
				factor = 1.0e24
			elif key == 'Orbital Inclination (degrees)':
				key = 'i'
			planet_dict[i-1][key] = parse_val(row[i]) * factor


moon_dict = {}
i_planet = 0
i_moon = 0
planet_name = planet_list[0]

# moon orbital file
with open('data/moons_orbital.txt', 'r') as f:
	moons_orbital = f.read()

for line in moons_orbital.split('\n'):
	if i_planet < len(planet_list) and planet_list[i_planet] in line:
		i_moon = 0
		planet_name = planet_list[i_planet]
		i_planet += 1
		moon_dict[planet_name] = {}
		continue
	row = re.split(r'\t', line)
	if row[0] == '':
		# print ' continuing'
		continue
	# print ' row: ' + str(row)
	moon_name = row[0].split(' ')[0]
	# print ' moon: ' + moon_name
	moon_dict[planet_name][moon_name] = {}
	moon_dict[planet_name][moon_name]['a'] = parse_val(row[4])
	moon_dict[planet_name][moon_name]['dia'] = parse_val(row[5])
	moon_dict[planet_name][moon_name]['number'] = i_moon
	i_moon += 1

i_planet = 0
i_moon = 0

# Physical data
with open('data/moons_physical.txt', 'r') as f:
	moons_physical = f.read()

from constants import G

for line in moons_physical.split('\n'):
	for j in range(len(fancy_planet_list)):
		fancy_planet_name = fancy_planet_list[j]
		singular_planet_name = planet_list[j]
		if fancy_planet_name in line or singular_planet_name in line:
			j_save = j
			i_planet += 1
			i_moon = 0
			break
	
	row = re.split(r'\t', line)
	if row[0] == '' or row[1] in ('GM', ''):
		continue

	planet_name = planet_list[j_save]
	moon_name = row[0].split(' ')[0]
	if moon_name not in moon_dict[planet_name]:
		continue
	
	moon_dict[planet_name][moon_name]['m'] = parse_val(row[1])/G
	moon_dict[planet_name][moon_name]['r'] = parse_val(row[3])
	moon_dict[planet_name][moon_name]['rho'] = parse_val(row[5])
	moon_dict[planet_name][moon_name]['albedo'] = parse_val(row[8])


for planet_name in copy(planet_list):
	for moon_name in copy(moon_dict[planet_name]):
		# Remove moons that are in the first source, but not the 2nd source
		#  (they can't be important, right?)
		if len(moon_dict[planet_name][moon_name].keys()) < 7:
			moon_dict[planet_name].pop(moon_name)

use_col = [
	'Mass (1024kg)',
	'Diameter (km)',
	'Distance from Sun (106 km)',
	'Orbital Inclination (degrees)',
	'dia', 'a', 'm', 'i'
]

print ' --planet list--'
print 'name\t' + '\t'.join([k for k in planet_dict[0].keys() if k in use_col])
for j in range(len(planet_dict)):
	print (planet_dict[j]['name'] + '\t' + '\t'.join([str(planet_dict[j][k])
		   for k in planet_dict[0].keys() if k in use_col]))

print '\n--moon data--'

moon_fields = moon_dict['Earth']['Moon'].keys()
print 'moon_name\tplanet_name\t' + '\t'.join(moon_fields)
for planet_name in planet_list:
	for moon_name in moon_dict[planet_name]:
		print (moon_name + '\t' + planet_name + '\t' + 
			   '\t'.join([str(moon_dict[planet_name][moon_name][k]) for k in
			   moon_dict[planet_name][moon_name].keys() if k in moon_fields]))
