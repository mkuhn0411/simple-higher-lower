import random
from art import logo
from art import vs
from game_data import data
from replit import clear
print(logo)

def get_random():
  return random.choice(data)

def compare_text(name, desc, country, letter):
  print(f"Compare {letter}: {name}, {desc}, from {country}")

def handle_guess(guess, comp_1, comp_2):
  highest_person = comp_1["name"] if comp_1["follower_count"] > comp_2["follower_count"] else comp_2["name"]
  guess_person = comp_1["name"] if guess == 'A' else comp_2["name"]
  return highest_person == guess_person

def get_guess(comp_1, comp_2):       
  compare_text(comp_1["name"],comp_1["description"], comp_1["country"],'A')
  print(vs) 
  compare_text(comp_2["name"],comp_2["description"], comp_2["country"],'B')
  guess = input("Who has more followers? Type 'A' or 'B': ")
  return guess

def print_right_text(score, guess_true):
  if guess_true:
    print(f"You're right! Current score {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")

def run():
  score = 0
  game_active = True
  comp_1 = get_random()
  comp_2 = get_random() 
  
  while game_active: 
    while comp_1 == comp_2:
      comp_2 = get_random()
    guess = get_guess(comp_1, comp_2)
    guess_true = handle_guess(guess, comp_1, comp_2)
    if guess_true:
      score += 1
      clear()
      print_right_text(score, guess_true)
      comp_1 = comp_2
      comp_2 = random.choice(data)
    else: 
      clear()
      print_right_text(score, guess_true)
      game_active = False

run()