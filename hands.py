from random import randint

def get_hands(num_of_players, banned, hands):
    if len(banned) > (71 - num_of_players):
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

def pick_card(hand, num_of_cards = 5):
    number = 1
    hand_string = []
    for card in hand.split('.'):
        with open("answers.txt") as file:
            card_text = file.read().split('\n')[int(card)]
        print(f"{number}) {card_text}")
        hand_string.append(card_text)
        number += 1
    
    print("\nWhat number card do you pick?: ", end = "")
    answer = input("").strip()
    integers = [str(num) for num in range(1, num_of_cards + 1)]
    while answer not in integers:
        print("That wasn't one of the options, please re-input: ", end = "")
        answer = input("").strip()

    print(f"You picked card {answer}: \"{hand_string[int(answer) - 1]}\"")
    return hand.split('.')[int(answer) - 1]

def get_prompt(banned):
    if len(banned) > (71 - num_of_players):
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