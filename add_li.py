import re
import sys

with open(sys.argv[1]) as f:
	with open('tmp', 'w') as af:
		af.write('<ul>\n')
		for l in f:
			if l != '\n':
				af.write('<li>\n{}\n</li>\n'.format(l.strip()))
		af.write('</ul>')
