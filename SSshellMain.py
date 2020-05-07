v = ""
while 1:
 oopen = open('SSshell.py', 'w')

 x = input('>>> ')

 def replace1():
  global x
  if 's.show-' in x:
   x = x.replace('s.show-', 'print')
  if 's.var-' in x:
   x = x.replace('s.var-', '')
  if 's.if-' in x:
   x = x.replace('s.if-', 'if ')
  if 's.elif-' in x:
   x = x.replace('s.elif-', 'elif ')
  if 's.else:' in x:
   x = x.replace('s.else:', 'else:')
  if 's.func-' in x:
   x = x.replace('s.func-', 'def ')
  if 's.r.func-' in x:
   x = x.replace('s.r.func-', '')
  if 's.class-' in x:
   x = x.replace('s.class-', 'class ')
  if 's.while-' in x:
   x = x.replace('s.while-','while ')
  if 's.plib-' in x:
   x = x.replace('s.plib-','import ')
  if 's.r.plib-' in x:
   x = x[9:]
  if 's.for-' in x:
   x = x.replace('s.for-','for ')
  if 's.skip-' in x:
   x = x.replace('s.skip-','pass ')
  if 's.replace-' in x:
   x = x.replace('s.return-','return ')
 replace1()
 v += x
 v += '\n'
 oopen.write(v)
 output = input('want to have output yet? y/n>>')
 if output == 'y':
  oopen.close()
 exec(open('SSshell.py', 'r').read())
