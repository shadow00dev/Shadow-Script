s.func-main():
  s.plib-random

  s.var-hidden = random.randrange(1,201)

  s.var-guess = int(input("<Guess the number>"))
  s.var-play = True

  s.while-play == True:
   s.if-guess == hidden:
    s.show-("welldone")
    s.var-hidden = random.randrange(1,201)
    s.var-guess = int(input("<Guess the number>"))    
   s.elif-guess < hidden:
    s.show-("to low")
    s.var-guess = int(input("<Guess the number>"))
   s.else:
    s.show-("to high")
    s.var-guess = int(input("<Guess the number>"))
s.r.func-main()
