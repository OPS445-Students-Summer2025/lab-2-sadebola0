#!/usr/bin/env python3
# Author: Sadam Adebola
# Author ID: sadebola@myseneca.ca
# Date Created: 2025/05/23

import sys

# Check if a command-line argument was provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

# Countdown loop
while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")

