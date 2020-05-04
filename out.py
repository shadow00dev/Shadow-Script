import os
def main():
 num1 = float(input('<num1>'))
 operator = str(input('<operator>'))
 num2 = float(input('<num2>'))
 if operator == '+':
   os.system('clear')
   print(num1 + num2)
   main()
 if operator == '-':
   os.system('clear')
   print(num1 - num2)
   main()
 if operator == '*':
  os.system('clear')
  print(num1 * num2)
  main()
main()
