from hand_identifier import *

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        return [self.rank, self.suit]


class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def update_hand_with_common_cards(self, common_cards, ranks):
        self.hand += common_cards
        self.hand.sort(key=lambda x: ranks.index(x.rank), reverse=True)

    def reset_hand(self, new_hand):
        self.hand = new_hand

    def show_hand(self):
        print([x.show() for x in self.hand])

    def get_hand_ranking(self):
        # Check for royal straight flush
        if is_royal_straight_flush(self.hand):
            return 9

        # Check for straight flush
        if is_straight_flush(self.hand):
            return 8

        # Check for four of a kind
        if is_four_of_a_kind(self.hand):
            return 7

        # Check for full house
        if is_full_house(self.hand):
            return 6

        # Check for flush
        if is_flush(self.hand):
            return 5

        # Check for straight
        if is_straight(self.hand):
            return 4

        # Check for three of a kind
        if is_three_of_a_kind(self.hand):
            return 3

        # Check for two pair
        if is_two_pair(self.hand):
            return 2

        # Check for one pair
        if is_one_pair(self.hand):
            return 1

        # Otherwise, it's a high card
        return 0