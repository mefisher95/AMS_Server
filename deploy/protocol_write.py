import sys

with open('Programs/Source/secure_dna_comparison.mpc', 'w') as comp1:
    code = '''
from Compiler.types import sint, regint, Array, MemValue
from Compiler.library import print_ln, do_while, for_range
from Compiler.util import if_else

DNA_LENGTH = {}
#client_sockets = Array(2, regint)
a = Array(DNA_LENGTH, sint)
b = Array(DNA_LENGTH, sint)


def difference(a, b, l):
    count = Array(1, sint)
    count[0] = 0
    @for_range(l)
    def loop_body(i):
        same = a[i] == b[i]
        count[0] = count[0] + same
    return DNA_LENGTH - count[0]
a.input_from(0)
b.input_from(1)
d = difference(a, b, DNA_LENGTH)
print_ln('the difference is %s', d.reveal())
'''.format(sys.argv[1])
    comp1.write(code)
    
with open('Programs/Source/secure_dna_comparison2.mpc', 'w') as comp2:
    code = '''
from Compiler.types import sint, regint, Array, MemValue
from Compiler.library import print_ln, do_while, for_range
from Compiler.util import if_else

DNA_LENGTH = {}
#client_sockets = Array(2, regint)
a = Array(2*DNA_LENGTH, sint)
b = Array(2*DNA_LENGTH, sint)


def difference(a, b, l):
    count = Array(1, sint)
    count[0] = 0
    c = Array(2, sint)
    @for_range(l)
    def loop_body(i):
        
        c[0] = a[2*i] + b[2*i] - 2*(a[2*i] * b[2*i])
        c[1] = a[2*i+1] + b[2*i+1] - 2*(a[2*i+1] * b[2*i + 1])
        different = c[0] + c[1] - c[0]*c[1]
        count[0] = count[0] + different
    return count[0]
a.input_from(0)
b.input_from(1)
d = difference(a, b, DNA_LENGTH)
print_ln('the difference is %s', d.reveal())

'''.format(sys.argv[1])
    comp2.write(code)

