import random

def play():
  user = input("What\'s your choice?\n'r' for rock, 'p' for paper, 's' for scissors\n")
  computer = random.choice(['r','p','s'])
  
  if user == computer:
    print('It\'s a tie')
    
  elif is_win(user, computer):
    print('You won!')

  else:
    print('You lost!')


def is_win(player, computer):
  #return True if the player wins
  #r>s, s>p, p>r

  if (player=='r' and computer =='s') or (player=='s' and computer =='p') or (player =='p' and computer =='r'):
    return True

play()