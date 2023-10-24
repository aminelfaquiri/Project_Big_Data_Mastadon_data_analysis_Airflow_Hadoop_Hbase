#!/usr/bin/env python3

import sys
import happybase


# Connect to HBase :
connection = happybase.Connection()
table = connection.table('content_lang')

def put_in_hbase(current_language,language_count) :
        table.put(
            current_language.encode('utf-8'),
            {
                b'language:lang_count': str(language_count).encode('utf-8'),

            }
        )




current_language = None
language_count = 0

for line in sys.stdin:
    try:
        language, count = line.strip().split("\t")

        # Si la langue change, émettre les résultats pour la langue précédente
        if current_language and language != current_language:
            #print(f"{current_language}\t{language_count}")
            put_in_hbase(current_language,language_count)
            language_count = 0

        current_language = language
        language_count += int(count)

    except:
        continue

# Émettre les résultats pour la dernière langue
if current_language:
    #print(f"{current_language}\t{language_count}")
    put_in_hbase(current_language,language_count)
