from pycompletbar import progressbar
from sys import argv

print(list(progressbar(*argv[1:])))
