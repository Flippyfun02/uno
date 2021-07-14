from colorama import Fore
import random

def print_color(hand):
  for card in hand:
    if card[0] == "R":
      card = Fore.RED + card + Fore.RESET
    elif card[0] == "G":
      card = Fore.GREEN + card + Fore.RESET
    elif card[0] == "B":
      card = Fore.BLUE + card + Fore.RESET
    elif card[0] == "Y":
      card = Fore.YELLOW + card + Fore.RESET
    
    print(card, end = " ")

def print_card(deck):
  print("Current Card: ", end = "")

  if deck[0][0] == "R":
    print(Fore.RED + deck[0] + Fore.RESET)
  elif deck[0][0] == "G":
    print(Fore.GREEN + deck[0] + Fore.RESET)
  elif deck[0][0] == "B":
    print(Fore.BLUE + deck[0] + Fore.RESET)
  elif deck[0][0] == "Y":
    print(Fore.YELLOW + deck[0] + Fore.RESET)

def valid(play, current_card):
  if play[0] != current_card[0] and play[1] != current_card[1]:
    return False
  else:
    return True

def find_card(card, hand):
  for i in range(len(hand)):
    if card in hand[i]:
      return i

def player_turn(deck, hand):
  print("\nYour turn...")
  print("Your Hand:", end = " ")
  print_color(hand)
  print("")

  if any(deck[0][0] in card for card in hand) or any(deck[0][1] in card for card in hand): # if choice is available
    play = input("Your Move: ").upper()
    while play not in hand:
      print("Please play a card in your hand.")
      play = input("Your Move: ").upper()
    while not valid(play, deck[0]):
      print("Please play a valid card.")
      play = input("Your Move: ").upper()
    # put at top of deck, then discard from hand
    deck += [deck.pop(0)] # current card goes to back of deck
    deck.insert(0, play)
    hand.pop(find_card(play, hand))
    
  else:
    print("Drawing new card...")
    # put og drawn card at the end of the pile
    # draw new one
    deck += [deck.pop(0)]
    play = deck[0]
    while not valid(play, deck[0]):
      play = deck[0]
      hand.append(play)
      deck.pop(0) # this card is now in hand
    # print new hand
    print("Your Hand:", end = " ")
    print_color(hand)
    print("")
  return deck, hand

def opp_turn(deck, oppHand):
  print("\nOpponent's turn...")

  if any(deck[0][0] in card for card in oppHand) or any(deck[0][1] in card for card in oppHand): # if choice is available
    random.shuffle(oppHand)
    for i in range(len(oppHand)): # find card
      if valid(oppHand[i], deck[0]):    
        # put at top of deck, then discard from hand
        deck += [deck.pop(0)] # current card goes to back of deck
        deck.insert(0, oppHand[i])
        oppHand.pop(i)
        break
    
  else:
    print("Drawing new card...")
    # put og drawn card at the end of the pile
    # draw new one
    deck += [deck.pop(0)]
    play = deck[0]
    while not valid(play, deck[0]):
      play = deck[0]
      oppHand.append(play)
      deck.pop(0) # this card is now in hand
  return deck, oppHand

def win(hand):
  if len(hand) == 1:
    print("Uno!")
    return False
  elif len(hand) == 0:
    return True
  else:
    return False