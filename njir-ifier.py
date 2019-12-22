import sys
import functools
import re

if len(sys.argv) == 1:
    print('Usage: python3 njir-ifier.py [filename]')
    sys.exit(1)

filename = sys.argv[1]

njir_contents = ''

try:
    njir_text = open(filename, 'r')
    njir_contents = njir_text.read()
except:
    print('File not found: {}'.format(filename))
    sys.exit(1)


print('Original:\n{}'.format(njir_contents))

njir_array = njir_contents.split(' ')

njir_mapped = map(lambda to_njir: re.sub('\w+', 'njir', to_njir), njir_array)

njir_ified = functools.reduce(lambda a, b : "{} {}".format(a, b), njir_mapped)

print('Njir-ified:\n{}'.format(njir_ified))
