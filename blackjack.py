import random
import time

game_deck = [("Ace of Spades", 1), ("Ace of Clubs", 1), ("Ace of Hearts", 1), ("Ace of Diamonds", 1),
        ("2 of Spades", 2), ("2 of Clubs", 2), ("2 of Hearts", 2), ("2 of Diamonds", 2),
        ("3 of Spades", 3), ("3 of Clubs", 3), ("3 of Hearts", 3), ("3 of Diamonds", 3),
        ("4 of Spades", 4), ("4 of Clubs", 4), ("4 of Hearts", 4), ("4 of Diamonds", 4),
        ("5 of Spades", 5), ("5 of Clubs", 5), ("5 of Hearts", 5), ("5 of Diamonds", 5),
        ("6 of Spades", 6), ("6 of Clubs", 6), ("6 of Hearts", 6), ("6 of Diamonds", 6),
        ("7 of Spades", 7), ("7 of Clubs", 7), ("7 of Hearts", 7), ("7 of Diamonds", 7),
        ("8 of Spades", 8), ("8 of Clubs", 8), ("8 of Hearts", 8), ("8 of Diamonds", 8),
        ("9 of Spades", 9), ("9 of Clubs", 9), ("9 of Hearts", 9), ("9 of Diamonds", 9),
        ("10 of Spades", 10), ("10 of Clubs", 10), ("10 of Hearts", 10), ("10 of Diamonds", 10),
        ("Jack of Spades", 10), ("Jack of Clubs", 10), ("Jack of Hearts", 10), ("Jack of Diamonds", 10),
        ("Queen of Spades", 10), ("Queen of Clubs", 10), ("Queen of Hearts", 10), ("Queen of Diamonds", 10),
        ("King of Spades", 10), ("King of Clubs", 10), ("King of Hearts", 10), ("King of Diamonds", 10)]

class Game:
    # Function to offer the user a complementary drink
    def offer_drink(self):
        drink_offer = ''
        while drink_offer != 'yes' or 'no':
            drink_offer = input('Server: "Would you like a drink on the house?" yes/no ')
            if drink_offer == 'yes':
                print("\nPouring your selected drink...\n")
                break
            elif drink_offer == 'no':
                print("\nNo problem. Enjoy the game!\n")
                break
            else:
                print("\nSorry, that answer is invalid. Please answer either 'yes' or 'no'.\n")

class Human:
    # Function to deal cards to the player
    def deal_player(self, player_hand=[]):
        self.player_hand = player_hand
        # Adding to player's hand
        self.player_hand.append(game_deck[0])
        # Removing from the game deck
        game_deck.remove(game_deck[0])
        # Repeating the process
        self.player_hand.append(game_deck[0])
        game_deck.remove(game_deck[0])

        # Showing the player their hand
        time.sleep(1)
        print("Here's your hand:\n")
        for card in self.player_hand:
            print(card[0])
        return self.player_hand

    # Function to deal cards to the dealer
    def deal_dealer(self, dealer_hand=[]):
        self.dealer_hand = dealer_hand

        time.sleep(1)
        print("\nThe dealer's being dealt a hand as well...\n")
        # Adding to dealer's hand
        self.dealer_hand.append(game_deck[0])
        # Removing from the game deck
        game_deck.remove(game_deck[0])
        # Repeating the process
        self.dealer_hand.append(game_deck[0])
        game_deck.remove(game_deck[0])

        # Showing the player only one of the dealer's cards
        time.sleep(1)
        print("This is one of the dealer's two cards:\n")
        print(f"{self.dealer_hand[0][0]}")
        return self.dealer_hand

    # Function that not only allows the player to 'hit' or 'stand', but also computes their hand value
    # Player will have the option to make Aces worth 1 or 11 if they choose
    def hit_player(self, player_hand, player_hand_value):
        hit_or_stand = ''
        # Flag to track whether or not the player is holding an Ace
        ace_flag = False
        # Flag to track whether or not the player has chosen to make one of their Aces equal 21
        ace_high = False
        # Check if the player is holding an Ace
        for card in player_hand:
            player_hand_value += card[1]
            if card[0] == "Ace of Spades":
                ace_flag = True
            elif card[0] == "Ace of Diamonds":
                ace_flag = True
            elif card[0] == "Ace of Hearts":
                ace_flag = True
            elif card[0] == "Ace of Clubs":
                ace_flag = True
        # If they are holding an Ace:
        if ace_flag == True:
            while True:
                ace_choice = input("\nWould you like to make your Ace worth 11? Enter 'yes' or 'no': ")
                # And they want it to be worth 21
                if ace_choice == 'yes':
                    # Add 10 to their hand value, and make the 'ace high' flag True
                    player_hand_value += 10
                    ace_high = True
                    break
                elif ace_choice == 'no':
                    break
                else:
                    print("\nSorry, that response is invalid.")
        # Blackjack if the player starts off with 21
        if player_hand_value == 21:
            print("\nYou've got Blackjack! Winner winner chicken dinner!\n")
            return False, player_hand_value
        # Run this loop as long as the player hasn't given an adequate response
        while hit_or_stand != 'hit' or 'stand':
            hit_or_stand = input("\nWould you like to hit or stand? Enter 'hit' or 'stand': ")
            # If player stands, show their hand and break the loop
            if hit_or_stand == 'stand':
                print("\nHere is your full hand:\n")
                for card in player_hand:
                    print(card[0])
                print(f"\nThe total value of your hand is {player_hand_value}")
                print("\nLet's see how you fare against the dealer...\n")
                break
            # If player hits, add to their hand and remove from the game deck
            elif hit_or_stand == 'hit':
                player_hand.append(game_deck[0])
                game_deck.remove(game_deck[0])
                # Storing the new card in a variable 'new card'
                new_card = player_hand[-1]
                print(f"\nThe {player_hand[-1][0]} was added to your hand.\n")
                print("Here is your full hand:\n")
                for card in player_hand:
                    print(card[0])
                # Condition for if the player hasn't made any Aces equal 21 yet
                if ace_high == False:
                    # Condition to make sure the player actually has an Ace
                    for card in player_hand:
                        if card[0] == "Ace of Spades":
                            ace_flag = True
                        elif card[0] == "Ace of Diamonds":
                            ace_flag = True
                        elif card[0] == "Ace of Hearts":
                            ace_flag = True
                        elif card[0] == "Ace of Clubs":
                            ace_flag = True
                    if ace_flag == True:
                        while True:
                            ace_choice = input("\nWould you like to make your Ace worth 11? Enter 'yes' or 'no': ")
                            # If the player has an Ace...
                            # AND they haven't made any of their Aces worth 21 yet...
                            # AND they're deciding to do that right now
                            # Then, we finally add 10 to their player hand value, and set the 'ace high' flag to True
                            if ace_choice == 'yes':
                                player_hand_value += 10
                                ace_high = True
                                break
                            elif ace_choice == 'no':
                                break
                            else:
                                print("\nSorry, that response is invalid.")
                # Card value gets added to the player's hand
                player_hand_value += new_card[1]
                print(f"\nThe current value of your cards is {player_hand_value}.")
                hit_or_stand = ''
                # If player gets 21, they win and end the game
                # By returning 'False', this allows us to immediately end the game once we return to the 'start_game' function
                if player_hand_value == 21:
                    print("\nYou've got exactly 21! Winner winner chicken dinner!\n")
                    return False, player_hand_value
                # If player exceeds 21, they bust and lose the game. Returning False allows us to immediately end the game
                elif player_hand_value > 21:
                    print("\nYou've gone bust! Better luck next time!\n")
                    return False, player_hand_value
            else:
                print("\nSorry, that response is invalid. Please try again")
        return player_hand, player_hand_value

    def hit_dealer(self, dealer_hand, dealer_hand_value):
        # Same as the player, the dealer needs an 'ace flag' to check whether or not they have an Ace
        ace_flag = False
        for card in dealer_hand:
            dealer_hand_value += card[1]
            if card[0] == "Ace of Spades":
                ace_flag = True
            elif card[0] == "Ace of Diamonds":
                ace_flag = True
            elif card[0] == "Ace of Hearts":
                ace_flag = True
            elif card[0] == "Ace of Clubs":
                ace_flag = True
        # Unlike the player, however, we automatically add 10 to the dealer's hand if they have an Ace
        # But if the dealer has two Aces, we only make one of them equal 11, and thus only add 10 once
        # The dealer will have the option later to make their Ace equal 1 again if they bust
        if ace_flag == True:
            dealer_hand_value += 10
        time.sleep(1)
        print("Here is the dealer's current hand:\n")
        for card in dealer_hand:
            print(card[0])
        # Dealer gets Blackjack, game automaticallly ends
        if dealer_hand_value == 21:
            print("\nThe dealer has Blackjack. Better luck next time!\n")
            return False, dealer_hand_value
        # Flag to check whether or not the dealer added any cards
        # If they didn't, there's no need to show their hand to the user again - because nothing changed
        dealer_added = False
        # Loop where dealer continues to add cards to their hand until it equals 17 or more
        while dealer_hand_value < 17:
            dealer_hand.append(game_deck[0])
            game_deck.remove(game_deck[0])
            new_card = dealer_hand[-1]
            time.sleep(2)
            print(f"\nA {dealer_hand[-1][0]} has just been added to the dealer's hand...\n")
            dealer_hand_value += new_card[1]
            # If the dealer busts, but they also have an Ace
            if ace_flag == True and dealer_hand_value > 21:
            # The Ace that was originally set to 11 now gets turned back to the value of 1
            # This gives the dealer a new chance to win
                dealer_hand_value -= 10
                # The 'ace flag' needs to be flipped back to False
                # Because we can only subtract 10 once from dealer's hand
                ace_flag = False
            dealer_added = True

        time.sleep(1)
        if dealer_added == True:
            print("Here is the dealer's full hand:\n")
            for card in dealer_hand:
                print(card[0])
        if dealer_hand_value > 21:
            print("\nThe dealer has busted. You win!\n")
            return False, dealer_hand_value
        else:
            return dealer_hand, dealer_hand_value
        
player1 = Human()
dealer1 = Human()
game1 = Game()

def start_game():
    print("\nHi there! Let's play some Black Jack!\n")
    print("The deck is currently being shuffled...\n")
    player_hand_value = 0
    dealer_hand_value = 0

    # Shuffling the deck
    random.shuffle(game_deck)
    time.sleep(1)
    
    game1.offer_drink()

    player_hand = player1.deal_player()
    dealer_hand = dealer1.deal_dealer()
    player_hand, player_hand_value = player1.hit_player(player_hand, player_hand_value)
    if player_hand == False:
        return
    dealer_hand, dealer_hand_value = dealer1.hit_dealer(dealer_hand, dealer_hand_value)
    if dealer_hand == False:
        return

    print(f"\nThe value of your hand is {player_hand_value}.")
    print(f"The value of the dealer's hand is {dealer_hand_value}\n")
    if player_hand_value > dealer_hand_value:
        print("Congratulations, you won!!\n")
    elif dealer_hand_value > player_hand_value:
        print("Sorry, you lost to the dealer. Play again and get revenge!\n")
    else:
        print("There was a draw between you and the dealer.\n")

start_game()