#!/usr/bin/env python3

import sys
import json
import re

# Regular expression pattern to match URLs
url_pattern = re.compile(r'http[s]?://([a-zA-Z0-9.-]+)')

for line in sys.stdin:
    try:
        data = json.loads(line)
        content = data["content"]

        if content:
            # Extract URLs from the content using the regex pattern
            urls = re.findall(url_pattern, content)

            for url in urls:
                # Emit domain name
                print(f"{url}\t1")
    except:
        continue
