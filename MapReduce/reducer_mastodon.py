#!/usr/bin/env python3
import sys

current_user = None
current_followers_count = 0

for line in sys.stdin:
    user_id, followers_count = line.strip().split("\t")
    followers_count = int(followers_count)

    if user_id == current_user:
        current_followers_count += followers_count
    else:
        if current_user:
            print(f"{current_user}\t{current_followers_count}")
        current_user = user_id
        current_followers_count = followers_count

if current_user:
    print(f"{current_user}\t{current_followers_count}")

