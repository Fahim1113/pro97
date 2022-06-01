import random
num = random.randint(0, 9)
chances = 5
while chances > 0:
  var1 = int(input('Enter your guess: '))
  if var1<num:
    print('Guess a number higher than',var1)
    chances -=1
  elif var1>num:
    print('Guess a number lower than',var1)
    chances -=1
  else:
    print('You guessed the number')
    break
if chances == 0:
  print('You lost. The number was',num)