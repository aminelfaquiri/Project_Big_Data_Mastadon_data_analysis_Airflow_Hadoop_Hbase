#!/usr/bin/env python3

import sys

current_user = None
total_engagement = 0
count = 0

for line in sys.stdin:
    try:
        user, engagement = line.strip().split('\t')
        engagement = "{:.2f}".format(engagement)
        
        if current_user == user:
            total_engagement += engagement
            count += 1
        else:
            if current_user:
                average_engagement = total_engagement / count
                print(f"{current_user}\t{average_engagement}")
            current_user = user
            total_engagement = engagement
            count = 1

    except ValueError:
        # Handle errors in case of incorrect input
        pass

if current_user:
    average_engagement = total_engagement / count
    print(f"{current_user}\t{average_engagement}")

