#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        language = data.get("language", "Unknown")

        # Émettre la langue du post avec un compteur de 1
        print(f"{language}\t1")
    except:
        continue
