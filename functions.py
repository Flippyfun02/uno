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
  else:
    print(card)

def valid(play, current_card, wild, choice):
  # if there are wild conditions
  if wild:
    if (play[0] == choice and len(play) < 4) or (play == "W" or play == "W+4"):
      return True
    else:
      return False
  elif (play[0] in ["R", "G", "B", "Y"]):
    if (len(play) == 2) and (play[0] == current_card[0] or play[1:] == current_card[1:]):
      # if regular card
      if (int(play[1]) < 9 and int(play[1]) > 0):
        return True
      elif play[1] == "X":
        return True
    # if card is +2 or reverse
    elif len(play) == 3 and (play[1:] in ["+2", "RV"]):
      return True
  # if wild card
  elif play == "W" or play == "W+4":
    return True
  return False

def find_card(card, hand):
  for i in range(len(hand)):
    if card in hand[i]:
      return i

def drawcard(current_card, hand, deck, wild, choice):
  print("\nDrawing new card...", end = "")
  # put current card at end of the pile
  # draw new card
  deck += [deck.pop(0)]
  play = deck[0]
  # while not a valid card
  while valid(play, current_card, wild, choice) == False:
    time.sleep(1)
    print(".", end = "")
    hand.append(play)
    deck.pop(0)
    play = deck[0] # this card is now in hand
  wild = False
  print("\nSuccess!")
  time.sleep(1)
  current_card = play
  return current_card, hand, deck, wild, choice

def player_turn(current_card, hand, deck, wild, choice, oppHand):
  while True:
    print("\nYour turn...")
    time.sleep(0.5)
    print("Your Hand:", end = " ")
    print_hand(hand)

    # C0-9, W, W+4, C[special_cards]
    # if any available card: if matches color or number, or is special
    if any(current_card[0] in card for card in hand) or any(current_card[1] in card for card in hand) or ("W" in hand) or ("W+4" in hand):
      play = input("\nYour Move: ").upper()
      while (play not in hand) or (valid(play, current_card, wild, choice) == False):
        print("Please play a valid card in your hand.")
        play = input("\nYour Move: ").upper()
      wild = False

      # play card
      deck += [deck.pop(0)]
      deck.insert(0, play)
      # find card, then remove it
      hand.pop(find_card(play, hand))

      if play == "W":
        wild = True
        choice = input("Choose the color: ").upper()
        while (choice not in ["R", "G", "B", "Y"]) or (len(choice) != 1): # if choice is valid
          print("Please select a valid color. Enter only the first letter.")
          choice = input("Choose the color: ").upper()
      elif play == "W+4":
        wild = True
        print("Drawing Opponent's Cards...")
        for i in range(4):
          oppHand.append(deck[1])
          deck.pop(1)
        choice = input("Choose the color: ").upper()
        while (choice not in ["R", "G", "B", "Y"]) or (len(choice) != 1):
          print("Please select a valid color. Enter only the first letter.")
          choice = input("Choose the color: ").upper()
        continue
      elif play[2:] == "+2":
        print("Drawing Opponent's Cards...")
        for i in range(2):
          oppHand.append(deck[1])
          deck.pop(1)
        continue # new turn
      elif play[2:] == "X":
        continue
      elif play[2:] == "RV":
        continue
      break
    
    else:
      current_card, hand, deck, wild, choice = drawcard(current_card, hand, deck, wild, choice)
      print("\nYour Hand: ", end = "")
      print_hand(hand)
    current_card = deck[0]
    break
  return current_card, hand, deck, wild, choice, oppHand

def opp_turn(current_card, oppHand, deck, wild, choice, hand):
  while True:
    print("\nOpponent's turn...")
    time.sleep(0.5)

    # if choice is available
    if any(current_card[0] in card for card in oppHand) or any(current_card[1] in card for card in oppHand) or ("W" in oppHand) or ("W+4" in oppHand):
      random.shuffle(oppHand)
      deck += [deck.pop(0)] # current card goes to back of deck
      for i in range(len(oppHand)): # find card
        if valid(oppHand[i], current_card, wild, choice):
          wild = False
          play = oppHand[i]
          # put at top of deck, then discard from hand
          deck.insert(0, oppHand[i])
          oppHand.pop(i)

          if play == "W":
            wild = True
            print_card(play)
            choice = random.choice(["R", "G", "B", "Y"])
            for i in ["R", "G", "B", "Y"]:
              if any(i in card for card in oppHand): # if RGBY exists in hand, then check if choice makes sense
                while not any(choice in card for card in oppHand):
                  choice = random.choice(["R", "G", "B", "Y"])
                print(f"Color: {choice}")
                break
          elif play == "W+4":
            wild = True
            print_card(play)
            print("Drawing your cards...")
            for i in range(4):
              hand.append(deck[1])
              deck.pop(1)
            choice = random.choice(["R", "G", "B", "Y"])
            for i in ["R", "G", "B", "Y"]:
              if any(i in card for card in oppHand): # if RGBY exists in hand, then check if choice makes sense
                while not any(choice in card for card in oppHand):
                  choice = random.choice(["R", "G", "B", "Y"])
                print(f"Color: {choice}")
                break
            continue
          elif play[2:] == "+2":
            print_card(play)
            print("Drawing your cards...")
            for i in range(2):
              hand.append(deck[1])
              deck.pop(1)
            continue
          elif play[2:] == "X":
            print_card(play)
            print("Your turn has been skipped.")
            continue
          elif play[2:] == "RV":
            print_card(play)
            print("Reverse! It's Opponent's turn again!")
            continue
          break
    
    else:
      current_card, oppHand, deck, wild, choice = drawcard(current_card, oppHand, deck, wild, choice)
    current_card = deck[0]
    break
  return current_card, oppHand, deck, wild, choice, hand

def win(hand):
  if len(hand) == 1:
    print("Uno!")
    return False
  elif len(hand) == 0:
    return True
  else:
    return False