# Medium Level Problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    char_counts = Counter(s)
    # Sort by counter first, then by name in case of tie
    char_counts = sorted(char_counts.items(), key=lambda item: (-item[1], item[0]))
    
    # Print the first 3 items
    for i in range(3):
        print(*char_counts[i])