#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n = int(input().strip())

m = n % 2

if m != 0:
    print("Weird")


if m == 0:
    if 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <=20:
        print('Weird')

    elif n > 20:
        print('Not Weird')
