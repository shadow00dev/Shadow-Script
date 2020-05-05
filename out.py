def main():
  import random
  hidden = random.randrange(1,201)
  guess = int(input("<Guess the number>"))
  play = True
  while play == True:
   if guess == hidden:
    play = False
    print("welldone")   
   elif guess < hidden:
    print("to low")
    guess = int(input("<Guess the number>"))
   else:
    print("to high")
    guess = int(input("<Guess the number>"))
main()
