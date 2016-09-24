from random import shuffle

# class Card:
#     def __init__(self, suit, num):
#         self.suit = suit
#         self.nnum = num

# def add_to_deck():


class Deck:
    def __init__(self):
        suits = ["clubs", "hearts", "spades", "diamonds"]
        card_nums = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        # card_nums = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
        self.deck = [(suit, card) for suit in suits for card in card_nums]


class Player:
    def __init__(self):
        self.money = 100
        self.hand = []
        self.hand_value = 0

# take tuple index1
# from
# add to hand value

    # def add_value(self, hand):

    def hit(self, mydeck):
        self.hand.append(mydeck.deck.pop(0))
        self.hand_value += self.hand[-1][1]
        print(self.hand)
        print(self.hand_value)

#########################
# class Card:
#     def __init__(self, suit, num):
#         self.suit = suit
#         self.num = num


def player_turn():
    while True:
        hit_or_stand = input("HIT or STAND? ").lower
        if hit_or_stand == "hit":
            # return player.hit(new_deck)
            # print(player.hand_value)
            print("testing")
            continue
        elif hit_or_stand == "stand":
            break
        else:
            continue


# IMPORTANT


def setup():
    new_deck = Deck()
    shuffle(new_deck.deck)
    player = Player()
    dealer = Player()
    # print(new_deck.deck)
    print("Welcome to blackjack")
    player.hit(new_deck)
    player.hit(new_deck)
    # print(player.hand_value)

    player_turn()

    if player.hand_value == 21:
        return False
    else:
        return True


# IMPORTANT

# def game()
playing = True
while playing:
    playing = setup()
    playing = False


# print(new_deck.deck)
