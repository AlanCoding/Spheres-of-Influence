import re

planet_list = ['Mercury', 'Venus', 'Earth', 
'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

fancy_planet_list = ['Mercuran', 'Venuian', 'Earth', 
'Martian', 'Jovian', 'Saturnian', 'Uranian', 'Neptunian', 'Pluto']

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
		for i in range(1, len(row)):
			planet_dict[i-1][row[0]] = row[i]

# print 'planetary data by planet:'
# for i in planet_dict:
# 	print ' planet name: ' + planet_dict[i]['name']
# 	print ' planet data: '
# 	print planet_dict[i]

with open('data/moons_orbital.txt', 'r') as f:
	moons_orbital = f.read()

with open('data/moons_physical.txt', 'r') as f:
	moons_physical = f.read()

moon_dict = {}
i_planet = 0
i_moon = 0
planet_name = planet_list[0]

for line in moons_orbital.split('\n'):
	if i_planet < len(planet_list) and planet_list[i_planet] in line:
		i_moon = 0
		planet_name = planet_list[i_planet]
		# print '   planet: ' + planet_name
		i_planet += 1
		moon_dict[planet_name] = {}
		continue
	row = re.split(r'\t', line)
	if row[0] == '':
		# print ' continuing'
		continue
	# print ' row: ' + str(row)
	moon_name = row[0]
	# print ' moon: ' + moon_name
	moon_dict[planet_name][moon_name] = {}
	moon_dict[planet_name][moon_name]['a'] = row[4]
	moon_dict[planet_name][moon_name]['dia'] = row[5]
	moon_dict[planet_name][moon_name]['number'] = i_moon
	i_moon += 1

for name in planet_list:
	print ' planet: ' + name
	print moon_dict[name]

i_planet = 0
i_moon = 0

for line in moons_physical.split('\n'):
	for j in range(len(fancy_planet_list)):
		fancy_planet_name = fancy_planet_list[j]
		if fancy_planet_name in line:
			j_save = j
			i_planet += 1
			i_moon = 0
			break
	
	row = re.split(r'\t', line)
	if row[0] == '' or row[1] in ('GM', ''):
		continue
	print ' row: ' + str(row)
	planet_name = planet_list[j_save]
	moon_name = row[0]
	
	if moon_name not in moon_dict[planet_name]:
		print ' mismatch: ' + str(moon_name) + ' planet: ' + planet_name
		continue
	
	moon_dict[planet_name][moon_name]['GM'] = row[2]
	moon_dict[planet_name][moon_name]['r'] = row[3]
	moon_dict[planet_name][moon_name]['rho'] = row[5]
	moon_dict[planet_name][moon_name]['albedo'] = row[8]
	
# Sat.	GM		Mean radius		Mean density	Magnitude		Geometric
#  row: ['Sinope', '0.005', '', '19', '[20]', '2.6', '18.2R', '[26]', '0.04', '']


