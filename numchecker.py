from time import sleep

low = 0
high = 100
ans = (low + high )// 2
iteration = 0
print("Please think of a number between 0 and 100!")
sleep(2)

while True:
  user_input = str(input(f"\nIs your secret number {ans}? \nEnter 'h' to indicate the guess is too high. \nEnter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly. \nYour answer: "))
  iteration += 1
  if user_input == 'h':
    high = ans
  elif user_input == 'l':
    low = ans
  elif user_input == 'c':
    print (f"\nI guessed on iteration {iteration}! \nI chose wisely!")
    break
  ans = (low + high)//2
  
