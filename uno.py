"""
To do:
- special cards
- fix drawing cards
  - while loop
  - play card
- make current_card
"""

from colorama import Fore
import random, functions

#Fore/ Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

# create a variable called deck
# the value is a list of all the uno cards NOT INCLUDING special cards like wild, reverse, etc.
# an uno card looks like this "R5" - Red 5
# the deck itself will look something like this
# R0, R1, ..., R9, B0, ...

# set up

deck = []
colors = ["R", "G", "B", "Y"]

for color in colors:
  for x in range(10):
    card = color + str(x)
    deck.append(card)

# randomize the deck of cards using a function from the random library
# create a variable called hand
# remove and add the top card from the deck to the hand variable 7 times

hand = []
random.shuffle(deck)

for i in range(7):
  hand.append(deck[0])
  deck.pop(0) # removes deck[0]

# print each card in the hand in its respective color
# you can use the if statements you made before, just change the variable names

# create the opponent's hand

oppHand = []
for i in range(6):
  oppHand.append(deck[0])
  deck.pop(0)

# draw first card and let player make next play
# put drawn card to the end of the deck, then remove played card from hand and to end of deck

print("\n\nDrawing Card...")

deckEnd = deck[0]
functions.print_card(deck)

while True:
  # player's turn
  deck, hand = functions.player_turn(deck, hand)
  if functions.win(hand):
    print("You Win!")
    break
  print("")
  functions.print_card(deck)

  # opponent's turn
  deck, oppHand = functions.opp_turn(deck, oppHand)
  if functions.win(hand):
    print("You Lose!")
    break
  print("")
  functions.print_card(deck)

  if deck[0] == deckEnd:
    random.shuffle(deck)