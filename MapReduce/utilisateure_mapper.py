#!/usr/bin/env python3
import sys
import json
from datetime import datetime

for line in sys.stdin:
    try:
        data = json.loads(line)
        user_id = data['account']['id']
        followers_count = data['account']['followers_count']

        user_created_at = data['account']['created_at']
        user_created_at = datetime.strptime(user_created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
        favorites_count = data['favourites_count']
        reblogs_count = data['reblogs_count']
        
        engagement_rate = (favorites_count + reblogs_count) / (followers_count if followers_count > 0 else 1)

        print(f"{user_id}\t{followers_count}\t{user_created_at}\t{engagement_rate}")

    except Exception as e:
        # Handle JSON parsing errors if necessary
        pass

