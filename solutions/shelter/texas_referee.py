""" --- Texas Referee --- Challenging

Texas hold'em is a variation of the standard card game
of poker. Two cards (hole cards) are dealt face down
to each player and then five community cards are placed
face-up by the dealer. And when all openings we need
to define what is the combination a player have.

You are given a sequence of 7 cards and you should choose
the best hand (5 cards) in it. Card sequence are described
as a string, where each card are defined by two character
- rank and suit. Cards separated by commas.

The descending ranks are:
    "A" (Ace), "K" (King), "Q" (Queen), "J" (Jack),
    "T" (Ten), and "9" to "2".
The descending suits are:
    "h" (hearts), "d" (diamonds), "c" (clubs), "s" (spades).

Texas hold'em uses the classical poker hand list:
Straight flush, Four of a kind, Full house, Flush, Straight,
Three of a kind, Two Pair, One Pair and High card.

Because of the presence of community cards in Texas hold'em,
different players' hands can often come very close in value.
As a result, it is common for kickers to be used to determine
the winning hand for cases where two or more hands tie.
A kicker is a card which is part of the five-card poker hand,
but is not used in determining a hand's rank. For instance,
in the hand A-A-A-K-Q, the king and queen are kickers.

In our version of Texas Hold'em cards of differing suits have
different values. This means that there is only ever one best
five-card hand to return. So "Td" is higher than "Tc",
but lower then "Jc".

Your goal is to choose the best hand with 5 cards and return
them as a string, where cards are separated by commas and
ordering from the highest to lowest value.

For example:
    We have two pair by queens (heart and spades) and eights
    (diamonds and clubs) and nine heart as a kicker.
The result:
    "Qh,Qs,9h,8d,8c". Be careful with order.

Input:              A list of cards as a string.
Output:             The best hand as a string.
How it is used:     This concept is a good example of combinatorial
                    optimisation process, and could come in handy
                    should you make a poker game in Python.
Precondition:       cards_quantity == 7
                    All cards correct and unique.

"""

RANKS = "23456789TJQKA"  # 1-13
SUITS = "scdh"


def my_solution(cards_str):
    from itertools import combinations

    def get_hand_weight(hnd):
        def get_card_weight(c):
            return RANKS.index(c) + 1

        def is_straight(h):
            return ''.join([i[0] for i in h]) in RANKS[::-1]

        def is_flush(h):
            return len(set([i[1] for i in h])) == 1

        def is_four_of_kind(h):
            ranks = [i[0] for i in h]
            counted_cards = {r: ranks.count(r) for r in set(ranks)}
            return max(counted_cards.values()) == 4

        def is_three_of_kind(h):
            ranks = [i[0] for i in h]
            counted_cards = {r: ranks.count(r) for r in set(ranks)}
            return max(counted_cards.values()) == 3

        def is_full_house(h):
            ranks = [i[0] for i in h]
            counted_cards = {r: ranks.count(r) for r in set(ranks)}
            sorted_cards = sorted(counted_cards, key=counted_cards.get, reverse=True)
            return counted_cards[sorted_cards[0]] == 3 and counted_cards[sorted_cards[1]] == 2

        def is_two_pairs(h):
            ranks = [i[0] for i in h]
            counted_cards = {r: ranks.count(r) for r in set(ranks)}
            sorted_cards = sorted(counted_cards, key=counted_cards.get, reverse=True)
            return counted_cards[sorted_cards[0]] == 2 and counted_cards[sorted_cards[1]] == 2

        def is_pair(h):
            ranks = [i[0] for i in h]
            counted_cards = {r: ranks.count(r) for r in set(ranks)}
            sorted_cards = sorted(counted_cards, key=counted_cards.get, reverse=True)
            return counted_cards[sorted_cards[0]] == 2 and counted_cards[sorted_cards[1]] < 2

        if is_straight(hnd) and is_flush(hnd):
            # From 6 686 105 to 17 383 873
            return 13907101 * get_card_weight(hnd[0][0])

        if is_four_of_kind(hnd):
            # From 8 023 326 to 69 535 504
            return 1337221 * 4 * get_card_weight(hnd[0][0]) + get_card_weight(hnd[-1][0])

        if is_full_house(hnd):
            # From 658 920 to 8 023 320 points
            return 1938 * (100 * 3 * get_card_weight(hnd[0][0]) + 10 * 2 * get_card_weight(hnd[-1][0]))

        if is_flush(hnd):
            # From 195 200 to 658 800
            return 12200 * sum([get_card_weight(i[0]) for i in hnd])

        if is_straight(hnd):
            # From 74 905 to 19 4753
            return 14981 * get_card_weight(hnd[0][0])

        if is_three_of_kind(hnd):
            # From 5 765 to 74 903
            return 1920 * 3 * get_card_weight(hnd[0][0]) + sum([get_card_weight(i[0]) for i in hnd[3:]])

        if is_two_pairs(hnd):
            # From 693 to 5 761
            return 115 * 2 * get_card_weight(hnd[0][0]) \
                   + 115 * 2 * get_card_weight(hnd[2][0]) + get_card_weight(hnd[-1][0])

        if is_pair(hnd):
            # From 59 to 683
            return 25 * 2 * get_card_weight(hnd[0][0]) \
                   + sum([get_card_weight(i[0]) for i in hnd[2:]])

        # From 15 to 55
        return sum([get_card_weight(i[0]) for i in hnd])

    cards = sorted(cards_str.split(','),
                   key=lambda x: (RANKS.index(x[0]), SUITS.index(x[1])), reverse=True)
    hands = {}

    for hand in combinations(cards, 5):
        hands[tuple(hand)] = get_hand_weight(hand)

    strong_hands = sorted(filter(lambda x: max(hands.values()) == hands[x], hands.keys()),
                          key=lambda c: [RANKS.index(i[0]) if i.isupper() else SUITS.index(i[1]) for i in c],
                          reverse=True)

    return ','.join(strong_hands[0])


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/texas-referee/publications/category/clear/
