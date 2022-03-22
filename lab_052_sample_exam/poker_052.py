#!/usr/bin/env python3

import sys
ranks = 'A23456789TJQK'
suits = 'CDHS'

cards = ''.join(sys.stdin.read().strip().split())

rank_val = {card[0]: cards.count(card) for card in cards if card in ranks}
print(max(rank_val.values()))
