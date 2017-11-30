import re
import sys

with open(sys.argv[1]) as f:
	s = f.read()

pattern = '\[{}[0-9]*\]'.format(sys.argv[2])

new_s = re.sub(pattern, '', s)
new_s = re.sub('Paper nominated for Best Paper Award', '<b>Paper nominated for Best Paper Award</b>', new_s)
new_s = re.sub('Best Paper Award', '<b>Best Paper Award</b>', new_s)
new_s = re.sub('Invited paper', '<b>Invited paper</b>', new_s)
new_s = re.sub('Special session', '<b>Special session</b>', new_s)
new_s = new_s.strip(' ')

with open('tmp', 'w') as f:
	f.write(new_s)

full_s = ''
with open('tmp') as f:
	for l in f:
		s = l.strip()
		s = '<li>'+s+'</li>'
		full_s = full_s + s
print full_s
