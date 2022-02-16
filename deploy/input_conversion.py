import sys

def convert(base, version):
    conversion_table = {'A': ['0', '0 0'], 'T': ['1', '0 1'], 'G': ['2', '1 0'], 'C': ['3', '1 1']}
    return conversion_table[base][version]
    
if len(sys.argv) > 2:
    version = int(sys.argv[1])
    player = sys.argv[2]
    x = ''
    with open('Player-Data/P{}-DNA'.format(player), 'r') as D:
        dna = D.read()
        for base in dna:
            x += convert(base, version)
            x += ' '
    with open('Player-Data/Input-P{}-0'.format(player), 'w') as to_write:
        to_write.write(x)
