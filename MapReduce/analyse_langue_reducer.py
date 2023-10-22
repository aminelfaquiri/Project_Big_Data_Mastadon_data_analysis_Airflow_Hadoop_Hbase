#!/usr/bin/env python3

import sys

current_language = None
language_count = 0

for line in sys.stdin:
    try:
        language, count = line.strip().split("\t")

        # Si la langue change, émettre les résultats pour la langue précédente
        if current_language and language != current_language:
            print(f"{current_language}\t{language_count}")
            language_count = 0

        current_language = language
        language_count += int(count)

    except:
        continue

# Émettre les résultats pour la dernière langue
if current_language:
    print(f"{current_language}\t{language_count}")
