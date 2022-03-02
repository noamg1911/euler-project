"""
FileName: Poker hands
Author: N.G 8.5.21
Purpose: Find how many hands does Player 1 win in the poker hands file
"""

import time

HIGH_CARD = 1
PAIR = 2
TWO_PAIR = 3
THREE = 4
STRAIGHT = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR = 8
STRAIGHT_FLUSH = 9

NUM_CARDS_HAND = 5
VALUE_INDEX = 0
SUIT_INDEX = 1
HAND_VAL_INDEX = 0
HAND_CARDS_INDEX = 1
CARDS = ''.join([str(num) for num in range(2, 10)] + list('TJQKA'))


def split_to_two_hands(hands_row: str) -> tuple:
    """
    Splits a string of cards to two different hands
    :param hands_row: The string of cards
    :return: A tuple of two poker hands
    """
    cards_in_hands = hands_row.split()
    first_hand = cards_in_hands[:NUM_CARDS_HAND]
    second_hand = cards_in_hands[NUM_CARDS_HAND:]
    return first_hand, second_hand


def get_sorted_cards(hand: list) -> list:
    """
    Sorts the hand through the known order of cards
    :param hand: The hand of cards
    :return: The sorted hand of cards
    """
    values = [card[VALUE_INDEX] for card in hand]
    val_indexes = [CARDS.index(value) for value in values]
    return [val for _, val in sorted(zip(val_indexes, values), reverse=True)]


def is_pair(hand: list) -> list:
    """
    Checks if a hand has a pair and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    values = [card[VALUE_INDEX] for card in hand]
    if len(set(values)) == NUM_CARDS_HAND - 1:
        for card in set(values):
            if values.count(card) == 2:
                values.remove(card)
                values.remove(card)
                return [card] * 2 + get_sorted_cards(values)
    return []


def is_two_pair(hand: list) -> list:
    """
    Checks if a hand has a two pair and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    values = [card[VALUE_INDEX] for card in hand]
    if len(set(values)) == NUM_CARDS_HAND - 2:
        pairs = []
        for card in set(values):
            if values.count(card) == 2:
                pairs.append(card)
                values.remove(card)
                values.remove(card)
        if len(pairs) == 2:
            sorted_pairs = get_sorted_cards(pairs)
            return sorted_pairs[0] * 2 + sorted_pairs[1] * 2 + values[0]
    return []


def is_three(hand: list) -> list:
    """
    Checks if a hand has a three of a kind and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    values = [card[VALUE_INDEX] for card in hand]
    if len(set(values)) == NUM_CARDS_HAND - 2:
        for card in set(values):
            if values.count(card) == 3:
                for i in range(3):
                    values.remove(card)
                return [card] * 3 + get_sorted_cards(values)
    return []


def is_straight(hand: list) -> list:
    """
    Checks if a hand has a straight and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    sorted_hand = get_sorted_cards(hand)
    return sorted_hand if ''.join(sorted_hand) in CARDS[::-1] else []


def is_flush(hand: list) -> list:
    """
    Checks if a hand has a flush and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    suits = [card[SUIT_INDEX] for card in hand]
    return get_sorted_cards(hand) if len(set(suits)) == 1 else []


def is_full_house(hand: list) -> list:
    """
    Checks if a hand has a full house and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    values = [card[VALUE_INDEX] for card in hand]
    sorted_cards = []
    if len(set(values)) == NUM_CARDS_HAND - 3:
        for card in set(values):
            if values.count(card) == 3:
                for i in range(3):
                    values.remove(card)
                    sorted_cards.append(card)
        for card in set(values):
            if values.count(card) == 2:
                for i in range(2):
                    values.remove(card)
                    sorted_cards.append(card)
    return sorted_cards


def is_four(hand: list) -> list:
    """
    Checks if a hand has a four of a kind and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    values = [card[VALUE_INDEX] for card in hand]
    sorted_cards = []
    if len(set(values)) == NUM_CARDS_HAND - 3:
        for card in set(values):
            if values.count(card) == 4:
                for i in range(4):
                    values.remove(card)
                sorted_cards = [card] * 4 + values[0]
    return sorted_cards


def is_straight_flush(hand: list) -> list:
    """
    Checks if a hand has a straight flush and if so returns its sorted value
    :param hand: The hand of cards
    :return: Either the sorted hand or an empty list
    """
    return is_flush(hand) if is_straight(hand) and is_flush(hand) else []


def get_hand_value(hand: list) -> tuple:
    """
    Gets the value of a hand of cards and its sorted order by strength
    :param hand: The hand of cards
    :return: A tuple of the hand's value and sorted hand (by strength)
    """
    if is_straight_flush(hand):
        return STRAIGHT_FLUSH, is_straight_flush(hand)
    elif is_four(hand):
        return FOUR, is_four(hand)
    elif is_full_house(hand):
        return FULL_HOUSE, is_full_house(hand)
    elif is_flush(hand):
        return FLUSH, is_flush(hand)
    elif is_straight(hand):
        return STRAIGHT, is_straight(hand)
    elif is_three(hand):
        return THREE, is_three(hand)
    elif is_two_pair(hand):
        return TWO_PAIR, is_two_pair(hand)
    elif is_pair(hand):
        return PAIR, is_pair(hand)
    return HIGH_CARD, get_sorted_cards(hand)


def who_wins(first_hand, second_hand):
    """
    Determines who wins between two hands
    :param first_hand: The first hand of cards
    :param second_hand: The second hand of cards
    :return: A boolean valueof whether the first hand won or lost
    """
    first_value = get_hand_value(first_hand)
    second_value = get_hand_value(second_hand)
    if first_value[HAND_VAL_INDEX] == second_value[HAND_VAL_INDEX]:
        for card in range(NUM_CARDS_HAND):
            if CARDS.index(first_value[HAND_CARDS_INDEX][card]) > \
               CARDS.index(second_value[HAND_CARDS_INDEX][card]):
                return True
            if CARDS.index(first_value[HAND_CARDS_INDEX][card]) < \
               CARDS.index(second_value[HAND_CARDS_INDEX][card]):
                return False
    return True if first_value[HAND_VAL_INDEX] > second_value[HAND_VAL_INDEX]\
        else False


def main():
    start = time.time()
    total_wins_first_player = 0
    with open('euler54_text.txt', 'r') as hands_file:
        for hands_row in hands_file:
            first_hand, second_hand = split_to_two_hands(hands_row)
            total_wins_first_player += who_wins(first_hand, second_hand)
    print(total_wins_first_player)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
