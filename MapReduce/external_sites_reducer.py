#!/usr/bin/env python3

import sys
import happybase


# Connect to HBase :
connection = happybase.Connection()
table = connection.table('external_links')

def put_in_hbase(current_url,current_count) :
        table.put(
            current_url.encode('utf-8'),
            {
                b'website:links_count': str(current_count).encode('utf-8'),

            }
        )


current_url = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    url, count = line.split("\t")

    if current_url == url:
        # Sum up the counts for the same URL
        current_count += int(count)
    else:
        if current_url:
            # Emit the URL and its total count
            #print(f"{current_url}\t{current_count}")
            put_in_hbase(current_url,current_count)
        current_url = url
        current_count = int(count)

# Don't forget to emit the last URL and its count
if current_url:
    #print(f"{current_url}\t{current_count}")
    put_in_hbase(current_url,current_count)



connection.close()
