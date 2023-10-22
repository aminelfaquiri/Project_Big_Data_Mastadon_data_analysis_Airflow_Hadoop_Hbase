#!/usr/bin/env python3

import sys

current_user_id = None
current_user_created_at = None

for line in sys.stdin:
    line = line.strip()
    user_id, user_created_at = line.split("\t")

    if current_user_id == user_id:
        # If the user ID is the same, keep the latest creation date
        current_user_created_at = max(current_user_created_at, user_created_at)
    else:
        if current_user_id:
            # Emit the unique user ID with its latest creation date
            print(f"{current_user_id}\t{current_user_created_at}")
        current_user_id = user_id
        current_user_created_at = user_created_at

# Don't forget to emit the last user ID and its creation date
if current_user_id:
    print(f"{current_user_id}\t{current_user_created_at}")
