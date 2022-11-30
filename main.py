import random
from art import logo
from art import vs
from game_data import data
from replit import clear
print(logo)

def shuffle_data():
  return random.sample(data, len(data))

def compare_text(name, desc, country, letter):
  print(f"Compare {letter}: {name}, {desc}, from {country}")

def handle_guess(guess_data):
  higher_count = max([guess_data[1]["follower_count"], guess_data[2]["follower_count"]])
  highest_person = guess_data[1]["name"] if guess_data[1]["follower_count"] == higher_count else guess_data[2]["name"]
  guess_person = guess_data[1]["name"] if guess_data[0] == 'A' else guess_data[2]["name"]
  return highest_person == guess_person

def get_guess(data, ind):
  comp_1 = data[ind]
  comp_2 = data[ind + 1]         
  compare_text(comp_1["name"],comp_1["description"], comp_1["country"],'A')
  print(vs) 
  compare_text(comp_2["name"],comp_2["description"], comp_2["country"],'B')
  guess = input("Who has more followers? Type 'A' or 'B': ")
  return [guess, comp_1, comp_2]

def print_right_text(score, guess_true):
  if guess_true:
    print(f"You're right! Current score {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")

def run():
  shuffled_data = shuffle_data()
  index = 0
  score = 0
  game_active = True
  
  while game_active:
    guess = get_guess(shuffled_data, index)
    guess_true = handle_guess(guess)
    if guess_true:
      score += 1
      index += 2
      print_right_text(score, guess_true)
    else: 
      print_right_text(score, guess_true)
      game_active = False

run()