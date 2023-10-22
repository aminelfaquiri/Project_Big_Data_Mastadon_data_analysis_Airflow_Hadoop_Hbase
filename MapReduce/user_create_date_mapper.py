#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        user_created_at = data["account"]["created_at"]
        user_id = data["account"]["id"]

        if user_created_at and user_id:
            # Emit user ID and user creation date
            print(f"{user_id}\t{user_created_at}")
    except:
        continue
