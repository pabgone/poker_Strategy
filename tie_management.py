
def get_highest_card_rank(cards, n):
    return max([card.rank for card in cards])


################################################## IN CASE OF TIE, IDENTIFY WINNER #############################################

def tie_straight_flush(*args):
    determiner, useful_cards = {}, {}
    for player in args:
        suit_counts = {card.suit: 0 for card in player.hand}
        for card in player.hand: suit_counts[card.suit] += 1
        useful_cards[player.name] = [card for card in player.hand if card.suit == max(suit_counts, key=suit_counts.get)]
        determiner[player.name] = get_highest_card_rank(useful_cards)

    max_score = max(determiner.values())
    potential_winners = {x: determiner[x] for x in determiner if determiner[x] == max_score}
    if len(potential_winners) == 1:
        winner = max(determiner, key=determiner.get)
        print("%s wins with a better straight flush: %s" % (list(potential_winners.keys())[0], useful_cards[winner]))
    else: print("%s have all the same straight flush" % (list(potential_winners.keys())))


def tie_four_of_a_kind(*args):
    determiner, useful_cards, other_cards = {}, {}, {}
    for player in args:
        rank_counts = {card.rank: 0 for card in player.hand}
        for card in player.hand: rank_counts[card.suit] += 1
        useful_cards[player.name] = [card for card in player.hand if card.rank == max(rank_counts, key=rank_counts.get)]
        determiner[player.name] = get_highest_card_rank(useful_cards)

    max_score = max(determiner.values())
    potential_winners = {x: determiner[x] for x in determiner if determiner[x] == max_score}
    if len(potential_winners) == 1:
        winner = max(determiner, key=determiner.get)
        print("%s wins with a better straight flush: %s" % (list(potential_winners.keys())[0], useful_cards[winner]))
    else:
        for player in args:
            other_cards[player.name] =  [x for x in player.hand if not any(x.rank == card.rank and x.suit == card.suit for card in useful_cards[player.name])]
            determiner[player.name] = get_highest_card_rank(other_cards[player.name])
            max_score = max(determiner.values())
            potential_winners = {x: determiner[x] for x in determiner if determiner[x] == max_score}
            if len(potential_winners) == 1:
                winner = max(determiner, key=determiner.get)
                print("%s wins with a hand: %s" % (list(potential_winners.keys())[0], winner.hand))
            else: print("%s have the same hand" %potential_winners)





def tie_full_house(*args):
    # Count the occurrences of each rank
    rank_counts = {card.rank: 0 for card in args}
    for card in args: rank_counts[card.rank] += 1

    # Check if there is a three of a kind and a pair
    return 3 in rank_counts.values() and 2 in rank_counts.values()


def tie_flush(*args):
    determiner, useful_cards = {}, {}
    for player in args:
        suit_counts = {card.suit: 0 for card in player.hand}
        for card in player.hand: suit_counts[card.suit] += 1
        useful_cards[player.name] = [card for card in player.hand if card.suit == max(suit_counts, key=suit_counts.get)]
        determiner[player.name] = get_highest_card_rank(useful_cards)

    max_score = max(determiner.values())
    potential_winners = {x: determiner[x] for x in determiner if determiner[x] == max_score}
    if len(potential_winners) == 1:
        winner = max(determiner, key=determiner.get)
        print("%s wins with a better flush: %s" % (list(potential_winners.keys())[0], useful_cards[winner]))
    else: print("%s have all the same flush" % (list(potential_winners.keys())))

#
# def tie_straight(*args):
#     # check straight, ['A', '2', '3', '4', '5'] is also a straight
#     ranks_order = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12,
#                    "A": 13}
#     ranks = list(set([card.rank for card in *args]))
#     ranks.sort(key=lambda x: ranks_order[x])
#     for i in range(len(ranks) - 4):
#         if ranks[i:i + 5] in sequences: return True
#     if all(card_rank in ranks for card_rank in ['A', '2', '3', '4', '5']): return True
#     return False
#
#
# def tie_three_of_a_kind(*args):
#     # Count the occurrences of each rank
#     rank_counts = {card.rank: 0 for card in *args}
#     for card in *args:
#         rank_counts[card.rank] += 1
#
#     # Check if there are three cards with the same rank
#     return 3 in rank_counts.values()
#
#
# def tie_two_pair(*args):
#     # Count the occurrences of each rank
#     rank_counts = {card.rank: 0 for card in *args}
#     for card in *args:
#         rank_counts[card.rank] += 1
#
#     # Check if there are two pairs
#     return len([x for x in rank_counts if rank_counts[x] == 2]) == 2
#
#
def tie_one_pair(*args):
    determiner, useful_cards, other_cards = {}, {}, {}
    for player in args:
        rank_counts = {card.rank: 0 for card in player.hand}
        for card in player.hand: rank_counts[card.suit] += 1
        useful_cards[player.name] = [card for card in player.hand if card.rank == max(rank_counts, key=rank_counts.get)]
        determiner[player.name] = get_highest_card_rank(useful_cards)

    max_score = max(determiner.values())
    potential_winners = {x: determiner[x] for x in determiner if determiner[x] == max_score}
    if len(potential_winners) == 1:
        winner = max(determiner, key=determiner.get)
        print("%s wins with a better straight flush: %s" % (list(potential_winners.keys())[0], useful_cards[winner]))
    else:
        for player in args:
            other_cards[player.name] = [x for x in player.hand if not any(
                x.rank == card.rank and x.suit == card.suit for card in useful_cards[player.name])]
            determiner[player.name] = get_highest_card_rank(other_cards[player.name])
            max_score = max(determiner.values())
            potential_winners = {x: determiner[x] for x in determiner if determiner[x] == max_score}
            if len(potential_winners) == 1:
                winner = max(determiner, key=determiner.get)
                print("%s wins with a hand: %s" % (list(potential_winners.keys())[0], winner.hand))
            else:
                print("%s have the same hand" % potential_winners)
#
#
