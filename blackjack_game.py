from random import shuffle

# class Card:
#     def __init__(self, suit, num):
#         self.suit = suit
#         self.nnum = num

# def add_to_deck():


class Deck:
    def __init__(self):
        suits = ["clubs", "hearts", "spades", "diamonds"]
        # card_nums = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card_nums = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
        self.deck = [(suit, card) for suit in suits for card in card_nums]


class Player:
    def __init__(self):
        self.money = 100
        self.hand = []
        self.hand_value = 0

    def get_value(self):
        return self.hand_value

# take tuple index1
# from
# add to hand value

    # def add_value(self, hand):

    def hit(self, mydeck):
        self.hand.append(mydeck.deck.pop(0))
        if self.hand[-1][1] == "jack":
            self.hand_value += 10
        elif self.hand[-1][1] == "queen":
            self.hand_value += 10
        elif self.hand[-1][1] == "king":
            self.hand_value += 10
        else:
            self.hand_value += self.hand[-1][1]
        print(self.hand)
        print(self.hand_value)
        # don't forget to add a face card value translator

    def hole(self, mydeck):
        self.hand.append(mydeck.deck.pop(0))
        if self.hand[-1][1] == "jack":
            self.hand_value += 10
        elif self.hand[-1][1] == "queen":
            self.hand_value += 10
        elif self.hand[-1][1] == "king":
            self.hand_value += 10
        else:
            self.hand_value += self.hand[-1][1]


#########################
# class Card:
#     def __init__(self, suit, num):
#         self.suit = suit
#         self.num = num


def player_turn(player, mydeck):
    while True:
        hit_or_stand = input("\nHIT or STAND? ").lower()
        if hit_or_stand == "hit":
            player.hit(mydeck)
            if player.hand_value < 21:
                continue
            else:
                print("BUST")
                break
        elif hit_or_stand == "stand":
            print("Your hand:")
            break
        else:
            continue


def dealer_turn(dealer, mydeck):
    print("\ndealers turn:")
    print("revealing hole card:")
    print(dealer.hand)
    print(dealer.hand_value)
    if dealer.hand_value < 17:
        while dealer.hand_value < 17:
            # print(dealer.hand)
            print("Drawing...")
            dealer.hit(mydeck)
    elif dealer.hand_value > 21:
        print("BUST")


# IMPORTANT


def setup():
    new_deck = Deck()
    shuffle(new_deck.deck)
    player = Player()
    dealer = Player()
    # print(new_deck.deck)
    print("Welcome to blackjack\n")

    print("Dealer hand:")
    dealer.hit(new_deck)
    dealer.hole(new_deck)
    if dealer.hand_value == 21:
        print("Dealer blackjack!")
        print(dealer.hand)
    else:
        print("?????????????")
        print("??hole card??")
        print("?????????????")

    print("\nYour hand:")
    player.hit(new_deck)
    player.hit(new_deck)
    if player.hand_value == 21:
        print("player blackjack!")
    # print(player.hand_value)

    player_turn(player, new_deck)

    dealer_turn(dealer, new_deck)
    # if player.hand_value > 21:
    #     return False
    # else:
    winner(player, dealer)
    # return True


def winner(player, dealer):

    if player.hand_value == dealer.hand_value and player.hand == 2:
        print("player blackjack! player wins")
        # player.money += 30

    elif player.hand_value == dealer.hand_value and dealer.hand == 2:
        print("dealer blackjack! dealer wins")
        # player.money -= 10

    elif player.hand_value == dealer.hand_value:
        print("It is a draw")

    elif player.hand_value > 21 and dealer.hand_value > 21:
        print("Double bust: no winners")

    elif player.hand_value > dealer.hand_value and player.hand_value < 22 or \
            player.hand_value < dealer.hand_value and dealer.hand_value > 21:
        print("\ndealer hand:")
        print(dealer.hand)
        print(dealer.hand_value)
        print("PLAYER WINS!")
        # player.money += 10

    elif player.hand_value < dealer.hand_value and dealer.hand_value < 22 or \
            player.hand_value > dealer.hand_value and player.hand_value > 21:
        print("\ndealer hand:")
        print(dealer.hand)
        print(dealer.hand_value)
        print("DEALER WINS")
        # player.money -= 10

    else:
        print("Bug!?!")

    print("Your total is ${}".format(player.money))


def game():
    playing = True
    while playing:
        playing = setup()
        ask = input("Play again? y/N: ").lower()
        if ask == "y":
            # play again
            playing = True
        elif ask == "n":
            playing = False
        else:
            playing = False
    else:
        print("\nThanks for playing")


game()
