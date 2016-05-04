import re

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

print 'planetary data by planet:'
for i in planet_dict:
	print ' planet name: ' + planet_dict[i]['name']
	print ' planet data: '
	print planet_dict[i]
