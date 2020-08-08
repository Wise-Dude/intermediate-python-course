import random

def main():
  player_1 = random.randint(1,6)
  player_2 = random.randint(1,6)

  if player_1 == player_2:
    print(f"It's a draw :( ")
    print(f"Player 1 rolled : {player_1} \nPlayer 2 rolled : {player_2}")
  elif player_1 > player_2:  
    print("Player 1 won! ")
    print(f"Player 1 rolled : {player_1} \nPlayer 2 rolled : {player_2}")
  else:
    print("player 2 won! ")
    print(f"Player 1 rolled : {player_1} \nPlayer 2 rolled : {player_2}")

if __name__== "__main__":
  main()
  