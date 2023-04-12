
from tie_management import *



poker_hands = {9: "Royal straight flush",
               8: "Straight flush",
               7: "Poker",
               6: "Full house",
               5: "Flush",
               4: "Straight",
               3: "Three of a kind",
               2: "Double pair",
               1: "Pair",
               0: "High card"}


def find_winning_hand(me, opponents):
    scores = {me.name: me.get_hand_ranking()}
    for opponent in opponents:
        scores[opponents[opponent].name] = opponents[opponent].get_hand_ranking()

    # max_score = max(scores, key=scores.get)
    max_score = max(scores.values())
    potential_winners = {x: scores[x] for x in scores if scores[x] == max_score}
    if len(potential_winners) == 1:
        print("%s wins" % list(potential_winners.keys())[0])
        print(scores)
    else:
        print("%s all have a %s" %(potential_winners, poker_hands[max_score]))
        if max_score == 8: tie_straight_flush(potential_winners)
        elif max_score == 7: tie_four_of_a_kind(potential_winners)
        # elif max_score == 6: tie_full_house(potential_winners)
        elif max_score == 5: tie_flush(potential_winners)
        # elif max_score == 4: tie_straight(potential_winners)
        # elif max_score == 3: tie_three_of_a_kind(potential_winners)
        # elif max_score == 2: tie_two_pair(potential_winners)
        # elif max_score == 1: tie_two_pair(potential_winners)
        # elif max_score == 0: tie_high_card(potential_winners)
        else: print("Something weird happened. Investigate.")





