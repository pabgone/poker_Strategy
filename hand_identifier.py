

sequences = [['2', '3', '4', '5', '6'], ['3', '4', '5', '6', '7'], ['4', '5', '6', '7', '8'],
             ['5', '6', '7', '8', '9'], ['6', '7', '8', '9', '10'], ['7', '8', '9', '10', 'J'],
             ['8', '9', '10', 'J', 'Q'], ['9', '10', 'J', 'Q', 'K'], ['10', 'J', 'Q', 'K', 'A']]


################################################## IDENTIFY HAND #############################################
def is_royal_straight_flush(hand):
    suit_counts = {card.suit: 0 for card in hand}
    for card in hand: suit_counts[card.suit] += 1
    check_flush = 5 in suit_counts.values()
    ranks_order = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12,
                   "A": 13}
    ranks = list(set([card.rank for card in hand]))
    ranks.sort(key=lambda x: ranks_order[x])
    if ['10', 'J', 'Q', 'K', 'A'] and check_flush: return True
    return False


def is_straight_flush(hand):
    # check flush
    suit_counts = {card.suit: 0 for card in hand}
    for card in hand: suit_counts[card.suit] += 1
    check_flush = 5 in suit_counts.values()

    # check straight, ['A', '2', '3', '4', '5'] is also a straight
    ranks_order = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12,
                   "A": 13}
    ranks = list(set([card.rank for card in hand]))
    ranks.sort(key=lambda x: ranks_order[x])
    for i in range(len(ranks) - 4):
        if ranks[i:i + 5] in sequences and check_flush: return True
    if all(card_rank in ranks for card_rank in ['A', '2', '3', '4', '5']) and check_flush: return True
    return False


def is_four_of_a_kind(hand):
    # Count the occurrences of each rank
    rank_counts = {card.rank: 0 for card in hand}
    for card in hand:
        rank_counts[card.rank] += 1

    # Check if there are four cards with the same rank
    return 4 in rank_counts.values()


def is_full_house(hand):
    # Count the occurrences of each rank
    rank_counts = {card.rank: 0 for card in hand}
    for card in hand: rank_counts[card.rank] += 1

    # Check if there is a three of a kind and a pair
    return 3 in rank_counts.values() and 2 in rank_counts.values()


def is_flush(hand):
    # Check if all cards have the same suit
    suit_counts = {card.suit: 0 for card in hand}
    for card in hand: suit_counts[card.suit] += 1
    return 5 in suit_counts.values()


def is_straight(hand):
    # check straight, ['A', '2', '3', '4', '5'] is also a straight
    ranks_order = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12,
                   "A": 13}
    ranks = list(set([card.rank for card in hand]))
    ranks.sort(key=lambda x: ranks_order[x])
    for i in range(len(ranks) - 4):
        if ranks[i:i + 5] in sequences: return True
    if all(card_rank in ranks for card_rank in ['A', '2', '3', '4', '5']): return True
    return False


def is_three_of_a_kind(hand):
    # Count the occurrences of each rank
    rank_counts = {card.rank: 0 for card in hand}
    for card in hand:
        rank_counts[card.rank] += 1

    # Check if there are three cards with the same rank
    return 3 in rank_counts.values()


def is_two_pair(hand):
    # Count the occurrences of each rank
    rank_counts = {card.rank: 0 for card in hand}
    for card in hand:
        rank_counts[card.rank] += 1

    # Check if there are two pairs
    return len([x for x in rank_counts if rank_counts[x] == 2]) == 2


def is_one_pair(hand):
    # Count the occurrences of each rank
    rank_counts = {card.rank: 0 for card in hand}
    for card in hand:
        rank_counts[card.rank] += 1

    # Check if there are two pairs
    return 2 in rank_counts.values()
