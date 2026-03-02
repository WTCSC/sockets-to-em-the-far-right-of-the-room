from random import randint

def get_hands(num_of_players, banned, hands):
    if len(banned) > 71 - num_of_players:
        del banned[:50]

    for player_num in range (0, num_of_players):
        hand = hands[player_num]

        while len(hand) < 5:
            new_card = randint(0, 71)
            if new_card not in banned:
                hand.append(new_card)
                banned.append(new_card)

        hands[player_num] = hand

    return hands, banned