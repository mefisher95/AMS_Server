import sys
import random

if len(sys.argv) > 2:
    bases = ['A', 'T', 'C', 'G']
    length = int(sys.argv[1])
    player = sys.argv[2]
    with open('Player-Data/P{}-DNA'.format(player), 'w') as to_write:
        for i in range(length):
            to_write.write(random.choice(bases))
    
