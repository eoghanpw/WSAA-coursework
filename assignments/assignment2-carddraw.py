# assignment2-carddraw.py
# Program that uses an API to deal 5 cards.
# Author: Eoghan Walsh
# References:
# https://deckofcardsapi.com/
# https://realpython.com/python-requests/#query-string-parameters

import requests
import numpy as np

# Shuffle the deck and deal 5 cards.
url = "https://deckofcardsapi.com/api/deck/new/draw/?count=5"
response = requests.get(url)
deal = response.json()
cards = deal["cards"]

values = []
suits = []

# Loop through to print cards and add to lists.
for card in cards:
    print(f"{card["value"]} {card["suit"]}")
    values.append(card["value"])
    suits.append(card["suit"])

# Congratulate user on a pair.
# Ref: https://www.geeksforgeeks.org/counting-number-of-unique-values-in-a-python-list/
pair = len(set(values))
if pair == 4:
    print("Congrats, a lovely pair!")

# Congratulate user on a flush.
flush = len(set(suits))
if flush == 1:
    print("OMG! You have drawn a flush!")

unique, count = np.unique(values, return_counts=True)

print(unique, count)
