# assignment2-carddraw.py
# Program that uses an API to deal 5 cards.
# Author: Eoghan Walsh
# References:
# [1] https://deckofcardsapi.com/
# [2] https://realpython.com/python-requests/#query-string-parameters
# [3] https://www.geeksforgeeks.org/counting-number-of-unique-values-in-a-python-list/
# [4] https://stackoverflow.com/a/51228746
# [5] https://www.geeksforgeeks.org/python-calculate-difference-between-adjacent-elements-in-given-list/

import requests
import numpy as np

# Shuffle the deck and deal 5 cards.
url = "https://deckofcardsapi.com/api/deck/new/draw/?count=5"  # Ref [1]

response = requests.get(url)  # Ref [2]
deal = response.json()
cards = deal["cards"]

# Loop through to print cards and add to lists.
values = []
suits = []
for card in cards:
    print(f"{card["value"]} {card["suit"]}")
    values.append(card["value"])
    suits.append(card["suit"])

# Congratulate user on a flush.
flush = len(set(suits))  # Ref [3]
if flush == 1:
    print("OMG! You have drawn a flush!")

# Congratulate user on a straight.
straight = []
for value in values:
    if value == "JACK":
        straight.append(11)
    elif value == "QUEEN":
        straight.append(12)
    elif value == "KING":
        straight.append(13)
    elif value == "ACE":
        straight.append(1)
    else:
        straight.append(int(value))

straight.sort()

straight = np.diff(np.array(straight)).tolist()  # Ref [5]

if straight == [1, 1, 1, 1]:
    print("Would you look at that! A straight!!")

# Congratulate user on a pair, 3/4 of kind & full house.
unique, counts = np.unique(values, return_counts=True)  # Ref [4]

pair_count = 0
three_count = 0
four_count = 0
for count in counts:
    if count == 2:
        pair_count += 1
    if count == 3:
        three_count += 1
    if count == 4:
        four_count += 1

if three_count == 1 and pair_count == 1:
    print("Full house!!!!!! Fantastic stuff!")
elif four_count == 1:
    print("Amazing, four of a kind!")
elif three_count == 1:
    print("Wow, three of a kind!")
elif pair_count == 2:
    print("Your luck is in, two pairs!")
elif pair_count == 1:
    print("Congrats, a lovely pair!")
