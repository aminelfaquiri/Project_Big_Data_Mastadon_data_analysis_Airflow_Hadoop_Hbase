#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        user_id = data['account']['id']
        favorites_count = data['favourites_count']
        reblogs_count = data['reblogs_count']
        followers_count = data['account']['followers_count']

        engagement_rate = (favorites_count + reblogs_count) / (followers_count if followers_count > 0 else 1)
        print(f"{user_id}\t{engagement_rate}")

    except Exception as e:
        # Handle JSON parsing errors if necessary
        pass

