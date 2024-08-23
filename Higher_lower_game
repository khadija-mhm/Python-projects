

from logo import logo
from logo import vs
import random
from game_data import data

#compare + guess
def compare():
  print(logo)
  print("Compare A: " + A["name"] + ", a " + A["description"] + ", from " + A["country"]+ ".")
  print(vs)
  print("Against B: " + B["name"] + ", a " + B["description"] + ", from " + B["country"] + ".")

#select
A = random.choice(data)
B = random.choice(data)
while A == B is True:
  B = random.choice(data)
score = 0
gameover = False
while gameover == False:
  compare()
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  if A["follower_count"] > B["follower_count"]:
    answer = "a"
    A = A
  if B["follower_count"] > A["follower_count"]:
    answer = "b"
    A = B
  if guess == answer:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
    gameover = True
  B = random.choice(data)
  if A == B:
    B = random.choice(data)



