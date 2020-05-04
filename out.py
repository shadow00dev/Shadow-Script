def main():
 num1 = float(input('<num1>'))
 operator = str(input('<operator>'))
 num2 = float(input('<num2>'))
 if operator == '+':
   print("[H[J")
   print(num1 + num2)
   main()
 if operator == '-':
   print("[H[J")
   print(num1 - num2)
   print("[H[J")
   main()
 if operator == '*':
  print("[H[J")
  print(num1 * num2)
  main()
main()
