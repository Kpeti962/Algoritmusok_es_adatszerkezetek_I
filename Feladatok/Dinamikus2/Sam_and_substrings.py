#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):

    mod = 10**9 + 7;
    vegosszeg = 0;
    aktual_osszeg = 0;
    
    
    for i in range(len(n)):
        aktual_szam = int(n[i]);
        aktual_osszeg = (aktual_osszeg * 10 + aktual_szam * (i + 1)) % mod;
        vegosszeg = (vegosszeg + aktual_osszeg) % mod;

    return vegosszeg;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
