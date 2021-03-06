"""
To do:
- fix errors
- fix aesthetic mess
"""

from colorama import Fore
import random, functions, time

# set up

deck = []
colors = ["R", "G", "B", "Y"]
special_cards = ["X", "+2", "RV"] # W, W+4

# creating deck
for color in colors:
  for x in range(10):
    card = color + str(x)
    deck.append(card)
  for y in special_cards:
    card = color + str(y)
    deck.append(card)
for i in range(4):
  deck.append("W+4")
  deck.append("W")

hand = []
random.shuffle(deck)

# creating hand
for i in range(7):
  hand.append(deck[0])
  deck.pop(0) # removes deck[0]

# create the opponent's hand
oppHand = []
for i in range(7):
  oppHand.append(deck[0])
  deck.pop(0)

# starting game
print("\nDrawing Card...")

current_card = deck[0]
while current_card in ["W", "W+4",] or current_card[1:] in special_cards:
  deck += [deck.pop(0)]
  current_card = deck[0]
deckEnd = current_card
time.sleep(1)
functions.print_card(current_card)

wild = False
choice = ""

while True:
  current_card = deck[0]

  # player's turn
  current_card, hand, deck, wild, choice, oppHand = functions.player_turn(current_card, hand, deck, wild, choice, oppHand)
  if functions.win(hand):
    print("You Win!")
    break
  print("")
  current_card = deck[0]
  functions.print_card(current_card)

  #opponent's turn
  current_card, oppHand, deck, wild, choice, hand = functions.opp_turn(current_card, oppHand, deck, wild, choice, hand)
  if functions.win(hand):
    print("You Lose!")
    break
  print("")
  current_card = deck[0]
  functions.print_card(current_card)

  if deck[0] == deckEnd:
    random.shuffle(deck)