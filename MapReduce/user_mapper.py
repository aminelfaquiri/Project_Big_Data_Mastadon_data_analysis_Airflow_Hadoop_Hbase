#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    data = json.loads(line)
    user_id = data["account"]["id"]
    followers_count = data["account"]["followers_count"]
    print(f"{user_id}\t{followers_count}")

