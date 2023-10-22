#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        media_attachments = data.get("media_attachments", [])
        post_id = data.get("id", "")

        if len(media_attachments) > 0:
            print(f"{post_id}\t1")
        else:
            print(f"{post_id}\t0")

    except:
        continue
