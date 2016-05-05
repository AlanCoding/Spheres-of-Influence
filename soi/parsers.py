import re

planet_list = ['Mercury', 'Venus', 'Earth', 
'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

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
	if i_planet >= len(planet_list):
		break
	if planet_list[i_planet] in line:
		i_moon = 0
		planet_name = planet_list[i_planet]
		print '   planet: ' + planet_name
		i_planet += 1
		moon_dict[planet_name] = {}
		continue
	row = re.split(r'\t', line)
	if row[0] == '':
		print ' continuing'
		continue
	print ' row: ' + str(row)
	moon_name = row[0]
	print ' moon: ' + moon_name
	moon_dict[planet_name][moon_name] = {}
	moon_dict[planet_name][moon_name]['a'] = row[4]
	moon_dict[planet_name][moon_name]['dia'] = row[5]

for name in planet_list:
	print ' planet: ' + name
	print moon_dict[name]


