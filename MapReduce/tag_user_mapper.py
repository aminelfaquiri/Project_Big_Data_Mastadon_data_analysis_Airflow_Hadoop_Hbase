#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        if "tags" in data:
            for tag in data["tags"]:
                # Emit tag as the key and "1" as the value
                print(f"#{tag}\t1")
                

        if "mentions" in data:
            if len(data["mentions"]) > 0 :
                for mention in data["mentions"]:
                    # Emit mentioned user as the key and "1" as the value
                    print(f"{mention}\t1")

    except:
        continue
