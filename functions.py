from colorama import Fore
import random, time

def print_hand(hand):
  for card in hand:
    if card[0] == "R":
      card = Fore.RED + card + Fore.RESET
    elif card[0] == "G":
      card = Fore.GREEN + card + Fore.RESET
    elif card[0] == "B":
      card = Fore.BLUE + card + Fore.RESET
    elif card[0] == "Y":
      card = Fore.YELLOW + card + Fore.RESET
    
    print(card, end = ", ")

def print_card(card):
  print("Current Card: ", end = "")

  if card[0] == "R":
    print(Fore.RED + card + Fore.RESET)
  elif card[0] == "G":
    print(Fore.GREEN + card + Fore.RESET)
  elif card[0] == "B":
    print(Fore.BLUE + card + Fore.RESET)
  elif card[0] == "Y":
    print(Fore.YELLOW + card + Fore.RESET)

def valid(play, current_card): # play[1] != current_card[1] ISSUE
  # if possible card
  if (len(play) == 2) and (play[0] in ["R", "G", "B", "Y"]) and (int(play[1]) < 9 and int(play[1]) > 0):
    if play[0] == current_card[0] or play[1] == current_card[1]:
        return True
  return False

def find_card(card, hand):
  for i in range(len(hand)):
    if card in hand[i]:
      return i

def drawcard(current_card, hand, deck):
  print("\nDrawing new card...", end = "")
  # put current card at end of the pile
  # draw new card
  deck += [deck.pop(0)]
  play = deck[0]
  # while not a valid card
  while valid(play, current_card) == False:
    time.sleep(1)
    print(".", end = "")
    hand.append(play)
    deck.pop(0)
    play = deck[0] # this card is now in hand
  print("\nSuccess!")
  time.sleep(1)
  current_card = play
  return current_card, hand, deck

def player_turn(current_card, hand, deck):
  print("\nYour turn...")
  time.sleep(0.5)
  print("Your Hand:", end = " ")
  print_hand(hand)

  # if any available card
  if any(current_card[0] in card for card in hand) or any(current_card[1] in card for card in hand):
    play = input("\nYour Move: ").upper()
    while (play not in hand) or (valid(play, current_card) == False):
      print("Please play a valid card in your hand.")
      play = input("\nYour Move: ").upper()
    deck += [deck.pop(0)]
    deck.insert(0, play)
    # find card, then remove it
    hand.pop(find_card(play, hand))
  
  else:
    current_card, hand, deck = drawcard(current_card, hand, deck)
    print("\nYour Hand: ", end = "")
    print_hand(hand)
  current_card = deck[0]
  return current_card, hand, deck

def opp_turn(current_card, oppHand, deck):
  print("\nOpponent's turn...")
  time.sleep(0.5)

  if any(current_card[0] in card for card in oppHand) or any(current_card[1] in card for card in oppHand): # if choice is available
    random.shuffle(oppHand)
    deck += [deck.pop(0)] # current card goes to back of deck
    for i in range(len(oppHand)): # find card
      if valid(oppHand[i], current_card):
        # put at top of deck, then discard from hand
        deck.insert(0, oppHand[i])
        oppHand.pop(i)
        break
  
  else:
    current_card, oppHand, deck = drawcard(current_card, oppHand, deck)
  current_card = deck[0]
  return current_card, oppHand, deck

def win(hand):
  if len(hand) == 1:
    print("Uno!")
    return False
  elif len(hand) == 0:
    return True
  else:
    return False