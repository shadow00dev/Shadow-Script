import os
import random
#opens files
IF_input = input('<<name of ss file>>') + '.ss'
os.system('clear')
print('the shadow script file', IF_input, 'has now be opened')
IF = open(IF_input, "rt")
OF = open("out.py", "wt")
OF.write('import os')
OF.write('\n')
#list of the "commands"
clist = ['s.show','s.var-','s.if-','s.func-','s.r.func','s.class-','s.os.clear','s.while-','s.plib-']
#changes words
for line in IF:

	if 's.show-' in line:
		OF.write(line.replace('s.show-', 'print'))
	if 's.var-' in line:
		OF.write(line.replace('s.var-', ''))
	if 's.if-' in line:
		OF.write(line.replace('s.if-', 'if '))
	if 's.func-' in line:
		OF.write(line.replace('s.func-', 'def '))
	if 's.r.func-' in line:
		OF.write(line.replace('s.r.func-', ''))
	if 's.class-' in line:
		OF.write(line.replace('s.class-', 'class '))
	if 's.os.clear' in line:
		OF.write(line.replace('s.os.clear',"os.system('clear')"))
	if 's.while-' in line:
		OF.write(line.replace('s.while-','while '))
	if 's.plib-' in line:
		OF.write(line.replace('s.plib-','import '))
	if 's.plib.r-' in line:
		OF.write(line[9:])

#closes files
IF.close()
OF.close()
#runs python file
exec(open("out.py").read())



