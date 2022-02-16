import sys
import random

if len(sys.argv) > 1:
    bases = ['A', 'T', 'C', 'G']
    length = int(sys.argv[1])
    for player in ['0', '1']:
        with open('Player-Data/P{}-DNA'.format(player), 'w') as to_write:
            for i in range(length):
                to_write.write(random.choice(bases))
    
