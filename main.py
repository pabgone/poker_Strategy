import random
import copy
from methods import Card, Player
from general_functions import find_winning_hand

# Define the deck of cards
suits = ["♥", "♦", "♣", "♠"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Your hand
my_hand = [Card("A", suits[0]), Card("K", suits[0])]
me = Player(copy.deepcopy(my_hand), "Pablo")

# Define the number of players in the table (excluding yourself), and number of simulations
num_players = 3
num_simulations = 50

# Create deck and initialize variables for studies
deck = [Card(rank, suit) for rank in ranks for suit in suits]
deck = [x for x in deck if not any(x.rank == card.rank and x.suit == card.suit for card in my_hand)]
wins = 0
total_hands = 0

# Run the simulations
for i in range(num_simulations):

    # Deal the hands for the other players
    opponents = {}
    opponents_hands_all = random.sample(deck, num_players * 2)
    opponents_hands = [opponents_hands_all[i:i + 2] for i in range(0, len(opponents_hands_all), 2)]
    for i, opponent_hand in enumerate(opponents_hands): opponents[i] = Player(opponent_hand, "Player %i" % i)

    # Update deck
    for opponent_hand in opponents_hands:
        for card in opponent_hand:
            deck = [x for x in deck if x.rank != card.rank or x.suit != card.suit]

    # Shuffle the deck
    random.shuffle(deck)

    # Deal the hand and the community cards. Burn cards in between. Flop (3 cards) + Turn (1 card) + River (1 card)
    # Now my hand and other players hand include these cards
    community_cards = deck[1:4] + [deck[5]] + [deck[7]]
    me.update_hand_with_common_cards(community_cards, ranks)
    for opponent in opponents: opponents[opponent].update_hand_with_common_cards(community_cards, ranks)

    # Check if your hand wins
    find_winning_hand(me, opponents)
    me.show_hand()
    for opponent in opponents: opponents[opponent].show_hand()

    # reset hand
    me.reset_hand(copy.deepcopy(my_hand))
    deck = [Card(rank, suit) for rank in ranks for suit in suits]
    deck = [x for x in deck if not any(x.rank == card.rank and x.suit == card.suit for card in my_hand)]

    print("\n")

#     for j in range(num_players):
#         if max(total_board[:5], key=lambda x: ranks.index(x.rank)) in other_hands[j]:
#             break
#     else:
#         wins += 1
#
#     total_hands += 1
#
# # Calculate the probability of winning
# win_probability = wins / total_hands
#
# # Print the result
# print("Hand: ", [card.rank + " of " + card.suit for card in hand])
# print("Number of players in the table: ", num_players)
# print("Number of simulations: ", num_simulations)
# print("Estimated probability of winning: {:.2%}".format(win_probability))
